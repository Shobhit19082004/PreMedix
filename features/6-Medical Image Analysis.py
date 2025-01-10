import streamlit as st
from google.generativeai import GenerativeModel
from dotenv import load_dotenv
import os
from PIL import Image
import io

# Load API key from environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    st.error("❌ Google API Key not found! Please configure the `.env` file with your API key.")
else:
    os.environ["GOOGLE_API_KEY"] = google_api_key

# Configure the Generative AI model
try:
    model = GenerativeModel(model_name="gemini-1.5-pro-latest")
except Exception as e:
    st.error(f"❌ Error initializing Generative AI model: {e}")

# Streamlit App Configuration
st.warning('⚠️Note: This Medical Image Assistant is powered by AI from PreMedix. Please use the results responsibly and seek professional medical advice if needed.')
# Header Section
# st.markdown("""
# <div style="text-align: center;">
#     <h1 style="font-size: 60px; color: #4A90E2;">🩺 <b>AI Medical Image Assistant</b></h1>
#     <h3 style="color: #7F8C8D;">Analyze Medical Images with AI-Powered Insights</h3>
# </div>
# <hr style='border: 2px solid #4A90E2; width: 60%; margin: auto;'>
# """, unsafe_allow_html=True)
st.header('🩻 Medical Image Assistant', anchor='medical-image-assistant', divider='rainbow')
with st.expander('What is Medical Image Assistant?'):
    st.write('The Medical Image Assistant is a Google AI based tool that analyzes and provides detailed insights, observations, recommendations, and treatment suggestions based on uploaded medical images such as X-rays, ultrasounds, and more. It aims to assist in understanding potential conditions but is not a replacement for professional medical diagnosis; always consult a healthcare professional for an accurate assessment and treatment plan."')
    # Symptom Details
st.write("Upload a Medical Image, and I'll provide detailed image analysis and advice.") 

# File Upload Section
st.markdown("<h2>📂 Upload Medical Images</h2>", unsafe_allow_html=True)
uploaded_files = st.file_uploader(
    "Upload medical images (PNG, JPG, JPEG)", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True)

# if uploaded_files:
#     st.markdown("<h3>🖼️ Uploaded Images</h3>", unsafe_allow_html=True)
#     for uploaded_file in uploaded_files:
#         try:
#             img = Image.open(uploaded_file)
#             st.image(img, caption=f"Uploaded: {uploaded_file.name}", use_column_width=True)
#         except Exception as e:
#             st.error(f"⚠️ Error loading image {uploaded_file.name}: {e}")
if uploaded_files:
    for uploaded_file in uploaded_files:
        # Set a specific width for the image display
        image_width = 400  # Adjust this value as needed
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=False, width=image_width)

    # Additional Details Section
    st.markdown("<h3>📝 Provide Additional Details (Optional)</h3>", unsafe_allow_html=True)
    additional_info = st.text_area(
        "Enter patient details, symptoms, or prior medical history:",
        placeholder="E.g., Patient age, gender, symptoms, or prior diagnoses"
    )

    # Analyze Button
    if st.button("🔍 Analyze Images"):
        st.markdown("⏳ **Analyzing images... Please wait.**")
        analysis_reports = []

        for uploaded_file in uploaded_files:
                image_data = uploaded_file.getvalue()
    
                # Prepare the analysis prompt
                analysis_prompt = f"""
                    You are a medical AI expert. Analyze the following medical image and additional information.
                    Additional Details: {additional_info or "No additional information provided."}
    
                    Instructions:
                    1. Provide a detailed analysis of the image.
                    2. List potential findings and observations.
                    3. Suggest recommendations, precautions and next steps.
                    4. Suggest Treatments or Medications if necessary.
                    5. Include a disclaimer: "Consult a qualified healthcare professional for a conclusive diagnosis."
                    """
    
                # Generate AI content
                response = model.generate_content(
                    [{"mime_type": "image/jpeg", "data": image_data},analysis_prompt],
                )
    
                if response and response.text:
                    analysis_reports.append({"name": uploaded_file.name, "report": response.text})
                else:
                    analysis_reports.append({"name": uploaded_file.name, "report": "Error: No response from AI model."})
            
        # Display Reports
        if analysis_reports:
            st.markdown("<h2>📋 Analysis Reports</h2>", unsafe_allow_html=True)
            for report in analysis_reports:
                st.markdown(f"<h4>🔎 Image: {report['name']}</h4>", unsafe_allow_html=True)
                st.write(report["report"])
                st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar FAQs
st.sidebar.markdown("<h2>📖 FAQs</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
<h4>1️⃣ What types of images can I upload?</h4>
<ul>
    <li>You can upload medical images such as X-rays, Ultrasound, CT scans, or MRI images in PNG, JPG, or JPEG format.</li>
</ul>
<h4>2️⃣ How accurate is the analysis?</h4>
<ul>
    <li>The analysis is AI-generated and provides general insights. It should not replace professional medical consultation.</li>
</ul>
<h4>3️⃣ Is this analysis confidential?</h4>
<ul>
    <li>Yes, the uploaded images are processed only for generating analysis and are not stored.</li>
</ul>
<h4>4️⃣ What additional information can I provide?</h4>
<ul>
    <li>Details like patient age, gender, symptoms, or prior medical history can improve the analysis quality.</li>
</ul>
""", unsafe_allow_html=True)
