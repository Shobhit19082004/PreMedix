import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import time

# Load API key from .env file
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if google_api_key:
    genai.configure(api_key=google_api_key)
else:
    raise ValueError("GOOGLE_API_KEY not found. Ensure it is set in the .env file.")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f9f9f9;
    }
    .header-title {
        font-size: 32px;
        color: #4CAF50;
        font-weight: bold;
    }
    .sub-header {
        font-size: 18px;
        font-weight: 500;
        margin-bottom: 15px;
    }
    .question-input {
        font-size: 16px;
        color: #4CAF50;
        font-weight: bold;
    }
    .bot-reply {
    font-size: 16px;
    color: #ffffff; /* Light text color for contrast */
    background-color: rgba(0, 123, 255, 0.6); /* Translucent blue */
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    }
    .analysis {
        font-size: 14px;
        color: #000;
        font-weight: 600;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.warning('⚠️Note: This Report Analyser AI is powered by AI from PreMedix. Please use the results responsibly and seek professional medical advice if needed.')
st.header('📄Report Analyser AI', anchor='report-analyser-ai', divider='rainbow')
with st.expander('What is Report Analyser AI?'):
    st.markdown(
        """
        <p class="description">
        The Report Analyser AI is a Google AI RAG-based tool that analyzes and provides detailed insights, explanations, 
        and recommendations based on uploaded medical reports such as pathology reports. 
        It aims to assist in understanding medical terminology, test results, conditions, and abnormalities present in the reports. 
        <b>Note:</b> It is not a replacement for professional medical diagnosis; always consult a healthcare professional 
        for an accurate assessment and treatment plan.
        </p>
        """,
        unsafe_allow_html=True,
    )

st.write(
    "<p class='sub-header'>Upload your Pathology Report, and I'll provide answers based on your queries related to the uploaded report.</p>",
    unsafe_allow_html=True,
)

# Function to extract text from uploaded PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into manageable chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save a FAISS vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to load the conversational chain
def get_conversational_chain():
    prompt_template = """
    You are an AI assistant trained in pathology analysis. Use the provided context to:
    1. Identify if the report is normal or abnormal.
    2. Explain medical terms and test results.
    3. Identify diseases, conditions, or abnormalities present in the report.
    4. Provide recommendations or next steps based on the report.
    5. Respond "Answer not available in the provided report" if insufficient context is found.

    Context: {context}
    Question: {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function for streaming responses
def stream_response(response_text):
    placeholder = st.empty()
    streamed_text = ""
    for word in response_text.split():
        streamed_text += f"{word} "
        placeholder.markdown(
            f"<p class='bot-reply'>{streamed_text}</p>", unsafe_allow_html=True
        )
        time.sleep(0.1)  # Simulate streaming delay

# Function to check for normal or abnormal conditions
def analyze_report_content(report_text):
    abnormal_indicators = ["high", "elevated", "low", "abnormal", "critical", "positive for"]
    normal_indicators = ["normal", "within range", "negative for"]

    for word in abnormal_indicators:
        if word in report_text.lower():
            return "Abnormalities detected in the report."

    for word in normal_indicators:
        if word in report_text.lower():
            return "The report appears normal."

    return "Unable to determine if the report is normal or abnormal."

# Sidebar for file upload and processing
with st.sidebar:
    st.markdown(
        "<div class='file-upload-section'>"
        "<h4>Upload & Process</h4>",
        unsafe_allow_html=True,
    )
    pdf_docs = st.file_uploader(
        "Upload your Pathology Reports (PDF only):", type=["pdf"], accept_multiple_files=True
    )
    if st.button("Submit & Process"):
        if pdf_docs:
            with st.spinner("Processing your report..."):
                try:
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Pathology reports processed successfully! You can now ask questions.")
                    st.session_state["report_text"] = raw_text
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.error("Please upload at least one pathology report.")
    st.markdown("</div>", unsafe_allow_html=True)

# User query section
st.subheader("Ask Your Questions:")
user_question = st.text_input("Type your question related to the uploaded report:")

if user_question and "report_text" in st.session_state:
    with st.spinner("Analyzing your query..."):
        try:
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
            docs = new_db.similarity_search(user_question)
            chain = get_conversational_chain()
            response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

            # Stream the bot's reply
            stream_response(response["output_text"])

            if "is the report normal" in user_question.lower():
                st.markdown(
                    f"<p class='analysis'>**Analysis:** {analyze_report_content(st.session_state['report_text'])}</p>",
                    unsafe_allow_html=True,
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
