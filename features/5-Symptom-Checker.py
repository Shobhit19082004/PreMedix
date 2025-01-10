import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to analyze symptoms
def analyze_symptoms(symptoms, duration, severity, medications, additional_info):
    """
    Analyze symptoms and provide possible conditions, precautions, and remedies.
    """
    try:
        # Construct the query with additional details
        prompt = f"""
        I have the following symptoms: {symptoms}.
        Duration: {duration}
        Severity: {severity}
        Medications taken: {medications}
        Additional Information: {additional_info}
        
        Provide a detailed analysis of possible conditions, precautions, and remedies. Include if immediate medical attention is required.
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
    # Symptom Details
    st.write("Describe your symptoms, and I'll provide possible conditions and advice.") 
    symptoms = st.text_area("📝 Describe your symptoms:", placeholder="E.g., headache, cough, fever")
    duration = st.selectbox("⏳ How long have you had these symptoms?", ["Less than a day", "1-3 days", "4-7 days", "More than a week"])
    severity = st.selectbox("⚠️ How severe are your symptoms?", ["Mild", "Moderate", "Severe"])
    medications = st.text_input("💊 Are you taking any medications?", placeholder="E.g., Paracetamol, Ibuprofen")
    additional_info = st.text_area("📝 Additional information (optional):", placeholder="E.g., recent travel, allergies, etc.")

    # Analyze Button
    if st.button("🔍 Analyze Symptoms"):
        if symptoms.strip():
            st.write("⏳ Analyzing symptoms... Please wait.")
            # Analyze Symptoms
            result = analyze_symptoms(symptoms, duration, severity, medications, additional_info)
            st.subheader("📋 Analysis Result:")
            st.write(result)
        else:
            st.warning("⚠️ Please describe your symptoms.")

elif page == "Health Tips":
    # Health Tips Page
    st.subheader("💡 Health Tips")
    tips_category = st.selectbox("📚 Category", ["General Health", "Diet", "Exercise", "Mental Health"])

    # Fetch Tips Button
    fetch_tips_button = st.button("💬 Get Tips")

    # Check if the button was clicked
    if fetch_tips_button:
        st.write("⏳ Fetching tips... Please wait.")
        tips = fetch_tips(tips_category)
        st.write(tips)
    elif not fetch_tips_button:
        # Empty space for tips if not fetched yet
        pass
