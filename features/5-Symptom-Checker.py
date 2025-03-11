import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Custom CSS for styling
st.markdown(
    """
     <style>
       .bot-reply {
            background-color: rgba(169, 169, 169, 0.5);  /* Translucent gray background */
            color: #000000;  /* Darker text color for better contrast */
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
            line-height: 1.6;
            margin-top: 5px;
            border: 1px solid rgba(169, 169, 169, 0.7);  /* Optional border for better visibility */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Google AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to stream the response
def stream_response(response_text):
    placeholder = st.empty()
    streamed_text = ""
    for word in response_text.split():
        streamed_text += f"{word} "
        placeholder.markdown(f"<p class='bot-reply'>{streamed_text}</p>", unsafe_allow_html=True)
        time.sleep(0.01)  # Simulate typing delay

# Function to analyze symptoms
def analyze_symptoms(symptoms, duration, severity, medications, additional_info):
    """
    Analyze symptoms and provide possible conditions, precautions, and remedies.
    """
    try:
        # Construct the query with additional details
        prompt = f""" You are a medical Ai Expert. Analyze the following symptoms and additional information.
        I have the following symptoms: {symptoms}.
        Duration: {duration}
        Severity: {severity}
        Medications taken: {medications}
        Additional Information: {additional_info}
        Instructions:
        1. Condition 1: [Description]
        2. Condition 2: [Description]
        3. Precautions: [Precaution 1, Precaution 2, ...]
        4. Suggest all the medicine related to the found disease.
        5. Remedies: [Remedy 1, Remedy 2, ...]
        6. Include if immediate medical attention is required.
        7. Include a disclaimer: "Consult a qualified healthcare professional for a conclusive diagnosis."
        
    
        """
        # AI Response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Function to fetch tips from API
def fetch_tips(category):
    """
    Fetch health tips from API based on selected category.
    """
    try:
        prompt = f"Provide health tips related to {category}. Include practical suggestions and recommendations."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit Web App UI
st.warning('⚠️Note: This symptom checker AI is powered by AI from PreMedix. Please use the results responsibly and seek professional medical advice if needed.')

# Sidebar Navigation
page = st.sidebar.radio("Select a page", ["Symptom Checker AI", "Health Tips"])

if page == "Symptom Checker AI":
    st.header('🤒 Symptom Checker AI', anchor='symptom-checker', divider='rainbow')
    with st.expander('What is Symptom Checker AI?'):
        st.write('The symptom checker AI is a Google AI based tool or system that helps users assess potential health conditions based on the symptoms they provide. It works by analyzing user-submitted symptoms, such as headaches, fever, or cough, and offering possible diagnoses, recommendations, or general health advice. The goal is to give users an understanding of what might be causing their symptoms and guide them on whether they should seek further medical attention.')

    st.write("Describe your symptoms, and I'll provide possible conditions and advice.") 
    symptoms = st.text_area("📝 Describe your symptoms:", placeholder="E.g., headache, cough, fever")
    duration = st.selectbox("⏳ How long have you had these symptoms?", ["Less than a day", "1-3 days", "4-7 days", "More than a week"])
    severity = st.selectbox("⚠️ How severe are your symptoms?", ["Mild", "Moderate", "Severe"])
    medications = st.text_input("💊 Are you taking any medications?", placeholder="E.g., Paracetamol, Ibuprofen")
    additional_info = st.text_area("📝 Additional information (optional):", placeholder="E.g., recent travel, allergies, etc.")
    # Sidebar FAQs
    st.sidebar.markdown("<h2>📖 FAQs</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("""
    <h4>1️⃣ What is Symptom Checker AI?</h4>
    <ul>
      <li> Symptom Checker AI is a tool that analyzes symptoms provided by the user to help identify possible conditions and remedies. It offers suggestions based on the symptoms you provide but is not a replacement for professional medical diagnosis.</li>
    </ul>
    <h4>2️⃣ How accurate is the Symptom Checker AI?</h4>
    <ul>
      <li> The Symptom Checker AI provides possible conditions based on your symptoms, but its accuracy depends on the details you provide. It is always best to consult a healthcare professional for a diagnosis.</li>
    </ul>
    <h4>3️⃣ Do I need to provide my complete medical history?</h4>
    <ul>
      <li> While it’s helpful to provide relevant details, you do not need to provide your entire medical history. Focus on the symptoms you're currently experiencing and any medications or treatments you're taking.</li>
    </ul>
    <h4>4️⃣ What additional information can I provide?</h4>
    <ul>
      <li>Details like patient age, gender or prior medical history can improve the analysis quality.</li>
    </ul>
""", unsafe_allow_html=True)

    # Analyze Button
    if st.button("🔍 Analyze Symptoms"):
        if symptoms.strip():
            with st.spinner("⏳ Analyzing symptoms... Please wait."):
            # Analyze Symptoms
             result = analyze_symptoms(symptoms, duration, severity, medications, additional_info)
             st.subheader("📋 Analysis Result:")
             stream_response(result)  # Stream the result
        else:
            st.warning("⚠️ Please describe your symptoms.")

elif page == "Health Tips":
    # Health Tips Page
    st.header("💡 Health Tips Generator",divider="rainbow")
    tips_category = st.selectbox("📚 Category", ["General Health", "Diet", "Exercise", "Mental Health"])

    # Fetch Tips Button
    fetch_tips_button = st.button("💬 Get Tips")
    st.sidebar.markdown("<h2>📖 FAQs</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("""
    <h4>1️⃣ What health categories do you provide tips on?</h4>
    <ul>
      <li> We provide health tips in the following categories: General Health, Diet, Exercise, and Mental Health.</li>
    </ul>
    <h4>2️⃣ Are the health tips personalized?</h4>
    <ul>
      <li> The health tips provided are general in nature. They are not personalized to your specific health condition. It’s always recommended to seek advice from a healthcare professional for personalized recommendations.</li>
    </ul>
    <h4>3️⃣ How can I get the most relevant health tips?</h4>
    <ul>
      <li> Select the category that best matches your current health needs. This will ensure the tips provided are more aligned with your situation.</li>
    </ul>
""", unsafe_allow_html=True)
    # Check if the button was clicked
    if fetch_tips_button:
        with st.spinner("⏳ Fetching tips... Please wait."):
            tips = fetch_tips(tips_category)
            stream_response(tips)  # Stream the tips response
    elif not fetch_tips_button:
        # Empty space for tips if not fetched yet
        pass
