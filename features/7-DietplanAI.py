import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get diet plan
def generate_diet_plan(disease):
    """
    Generates a diet plan for a person based on the given health issue.
    """
    try:
        prompt = f"""
        I am a healthcare assistant bot. A person has the following condition: {disease}.
        Provide a one-day diet plan including breakfast, lunch, dinner, and snacks.
        Ensure the plan is nutritious and supports recovery from the condition.
        """
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating diet plan: {e}"

# Streamlit UI
st.warning('⚠️Note: This Diet Planner AI is powered by AI from PreMedix. The suggested diet plans are AI-generated and should not replace medical advice. Consult a dietitian or healthcare professional for personalized recommendations.')

st.header('🍽️ Diet Planner AI', anchor='diet-planner-ai', divider='rainbow')
with st.expander('What is Diet Planner AI?'):
    st.write('The Diet Planner AI is a Google AI based tool that generates personalized daily diet plans based on your health conditions, such as fever, dengue, COVID-19, and other diseases, offering tailored food and nutritional recommendations to support recovery and overall well-being. While the AI aims to provide helpful dietary suggestions, it is not a substitute for professional medical or nutritional advice; always consult a healthcare provider for an accurate treatment and diet plan.')
    # Symptom Details
st.write("Provide your health issues, and I'll provide you the diet plan for a day.") 

# User input
disease = st.text_input("🔍 Enter your health issue (e.g., fever, dengue, diabetes):", key="disease_input")

# Get Diet Plan
if st.button("Generate Diet Plan"):
    if disease.strip():
        st.write("⏳ Generating your personalized diet plan... Please wait.")
        diet_plan = generate_diet_plan(disease)
        st.subheader("🍴 Your Diet Plan for the Day:")
        st.write(diet_plan)
    else:
        st.warning("⚠️ Please enter a health issue to generate a diet plan.")

