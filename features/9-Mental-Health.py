# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# import time

# # Load environment variables
# load_dotenv()

# # Configure Gemini API
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Streamlit UI
# st.warning('⚠️Note: This Mental Health AI is powered by AI from PreMedix.The suggestions are AI-generated and should not replace professional advice. Consult a mental health professional for personalized recommendations.')
# st.header('🙇🏻‍♂️ Mental Health AI', anchor='menntal-health-ai', divider='rainbow')
# with st.expander('What is Menatl Health AI?'):
#     st.write('The Mental Health AI is a Google AI based tool designed to help users manage stress and improve mental well-being. It offers personalized advice, stress management tips, and guided relaxation exercises such as deep breathing, progressive muscle relaxation, and visualization techniques. Additionally, the bot provides practical insights into common stress-related questions through an FAQ section, empowering users to handle stress effectively in their daily lives. While it aims to promote relaxation and mindfulness, the bot also encourages seeking professional help when stress becomes overwhelming or persistent.')
#     # Symptom Details
# st.write("Provide your Mental helath related issues, and I'll provide you some best recommendations.") 

# # Sidebar Navigation
# st.sidebar.title("Stress Relief Bot")
# page = st.sidebar.radio("Navigate", ["Stress Management Tips", "Relaxation Exercises", "FAQs"])

# # Stress management tips
# stress_tips = [
#     "Practice deep breathing: Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds.",
#     "Take a short walk outdoors to clear your mind.",
#     "Limit screen time and take regular breaks.",
#     "Maintain a gratitude journal to focus on positive aspects of your day.",
#     "Practice mindfulness or meditation for 5-10 minutes daily."
# ]

# # Relaxation exercises
# relaxation_exercises = [
#     "Progressive Muscle Relaxation: Tense and relax each muscle group from head to toe.",
#     "Visualization: Imagine yourself in a calm and peaceful place, like a beach or forest.",
#     "Yoga: Perform simple poses like child's pose, cat-cow stretch, or downward dog.",
#     "Guided Meditation: Use apps like Headspace or Calm for structured relaxation sessions.",
#     "Listening to calming music or nature sounds for 10-15 minutes."
# ]

# # FAQ section
# faq = {
#     "What is stress?": "Stress is the body's natural response to challenging situations. It can be physical, emotional, or mental.",
#     "What are common signs of stress?": "Signs of stress include irritability, fatigue, difficulty concentrating, sleep problems, and physical symptoms like headaches.",
#     "How can I reduce stress quickly?": "Quick stress relief methods include deep breathing, listening to calming music, or engaging in light physical activity.",
#     "When should I seek professional help?": "If stress is interfering with your daily life or causing severe symptoms, consider consulting a mental health professional."
# }

# # Function to generate personalized advice
# def generate_advice(prompt):
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"Error: {e}"

# # Main Page
# if page == "Stress Management Tips":
#     st.header("💡 Stress Management Tips")
#     st.write("Here are some quick tips to help you manage stress effectively:")
#     for tip in stress_tips:
#         st.markdown(f"- {tip}")
#     st.write("Got a specific question? Ask below!")
#     user_query = st.text_input("Ask about stress management:", placeholder="E.g., How can I manage stress at work?")
#     if user_query and st.button("Submit"):
#         with st.spinner("Generating advice..."):
#             prompt = f"Provide stress management advice for: {user_query}"
#             result = generate_advice(prompt)
#             st.subheader("🧘 Advice:")
#             st.write(result)

# elif page == "Relaxation Exercises":
#     st.header("🧘 Relaxation Exercises")
#     st.write("Try these exercises to relax and reduce stress:")
#     for exercise in relaxation_exercises:
#         st.markdown(f"- {exercise}")
#     st.write("Need more relaxation techniques? Ask below!")
#     user_query = st.text_input("Ask about relaxation techniques:", placeholder="E.g., How to calm my mind quickly?")
#     if user_query and st.button("Submit"):
#         with st.spinner("Generating techniques..."):
#             prompt = f"Provide relaxation techniques for: {user_query}"
#             result = generate_advice(prompt)
#             st.subheader("🌿 Techniques:")
#             st.write(result)

# elif page == "FAQs":
#     st.header("📋 Frequently Asked Questions")
#     st.markdown("""
# <h4>1️⃣ What types of images can I upload?</h4>
# <ul>
#     <li>You can upload medical images such as X-rays, Ultrasound, CT scans, or MRI images in PNG, JPG, or JPEG format.</li>
# </ul>
# <h4>2️⃣ How accurate is the analysis?</h4>
# <ul>
#     <li>The analysis is AI-generated and provides general insights. It should not replace professional medical consultation.</li>
# </ul>
# <h4>3️⃣ Is this analysis confidential?</h4>
# <ul>
#     <li>Yes, the uploaded images are processed only for generating analysis and are not stored.</li>
# </ul>
# <h4>4️⃣ What additional information can I provide?</h4>
# <ul>
#     <li>Details like patient age, gender, symptoms, or prior medical history can improve the analysis quality.</li>
# </ul>
# """, unsafe_allow_html=True)
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# System Instructions for AI Behavior
system_instructions = """
You are a Mental Health AI assistant designed to provide supportive, empathetic, and constructive responses.
Your role is to offer stress relief tips, relaxation exercises, and general mental health guidance.
Your responses should be friendly, easy to understand, and supportive, while also encouraging professional help when necessary.
"""

# System Configuration for AI Model
system_configuration = {
    #"temperature": 0.7,  
    "max_output_tokens": 500, 
    "top_p": 0.9,  
    "top_k": 50  
}

# Streamlit UI
st.warning('⚠️ **Note:** This Mental Health AI is powered by AI from PreMedix. The suggestions are AI-generated and should not replace professional advice. Consult a mental health professional for personalized recommendations.')

st.header('🙇🏻‍♂️ Mental Health AI', anchor='mental-health-ai', divider='rainbow')

with st.expander('What is Mental Health AI?'):
    st.write(
        "The Mental Health AI is a Google AI-based tool designed to help users manage stress and improve mental well-being. "
        "It offers personalized advice, stress management tips, and guided relaxation exercises such as deep breathing, progressive muscle relaxation, and visualization techniques. "
        "Additionally, the bot provides practical insights into common stress-related questions through an FAQ section, empowering users to handle stress effectively in their daily lives. "
        "While it aims to promote relaxation and mindfulness, the bot also encourages seeking professional help when stress becomes overwhelming or persistent."
    )

st.write("💭 Provide your mental health-related concerns, and I'll offer some personalized recommendations.")

# Sidebar Navigation
st.sidebar.title("Mental Health AI")
page = st.sidebar.radio("Navigate", ["Stress Management Tips", "Relaxation Exercises", "FAQs"])

# Stress management tips
stress_tips = [
    "Practice deep breathing: Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds.",
    "Take a short walk outdoors to clear your mind.",
    "Limit screen time and take regular breaks.",
    "Maintain a gratitude journal to focus on positive aspects of your day.",
    "Practice mindfulness or meditation for 5-10 minutes daily."
]

# Relaxation exercises
relaxation_exercises = [
    "Progressive Muscle Relaxation: Tense and relax each muscle group from head to toe.",
    "Visualization: Imagine yourself in a calm and peaceful place, like a beach or forest.",
    "Yoga: Perform simple poses like child's pose, cat-cow stretch, or downward dog.",
    "Guided Meditation: Use apps like Headspace or Calm for structured relaxation sessions.",
    "Listening to calming music or nature sounds for 10-15 minutes."
]

# FAQ section
faq = {
    "What is stress?": "Stress is the body's natural response to challenging situations. It can be physical, emotional, or mental.",
    "What are common signs of stress?": "Signs of stress include irritability, fatigue, difficulty concentrating, sleep problems, and physical symptoms like headaches.",
    "How can I reduce stress quickly?": "Quick stress relief methods include deep breathing, listening to calming music, or engaging in light physical activity.",
    "When should I seek professional help?": "If stress is interfering with your daily life or causing severe symptoms, consider consulting a mental health professional."
}

# Function to generate AI-based advice
def generate_advice(prompt):
    try:
        response = model.generate_content(
            f"{system_instructions}\n\nUser Query: {prompt}"
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Main Page Logic
if page == "Stress Management Tips":
    st.header("💡Stress Management Tips")
    st.write("Here are some quick tips to help you manage stress effectively:")
    for tip in stress_tips:
        st.markdown(f"- {tip}")
    st.write("Got a specific question? Ask below!")

    user_query = st.text_input("Ask about stress management:", placeholder="E.g., How can I manage stress at work?")
    if user_query and st.button("Submit"):
        with st.spinner("Generating advice..."):
            prompt = f"Provide stress management advice for: {user_query}"
            result = generate_advice(prompt)
            st.subheader("🧘 Advice:")
            st.write(result)

elif page == "Relaxation Exercises":
    st.header("🧘 Relaxation Exercises")
    st.write("Try these exercises to relax and reduce stress:")
    for exercise in relaxation_exercises:
        st.markdown(f"- {exercise}")
    st.write("Need more relaxation techniques? Ask below!")

    user_query = st.text_input("Ask about relaxation techniques:", placeholder="E.g., How to calm my mind quickly?")
    if user_query and st.button("Submit"):
        with st.spinner("Generating techniques..."):
            prompt = f"Provide relaxation techniques for: {user_query}"
            result = generate_advice(prompt)
            st.subheader("🌿 Techniques:")
            st.write(result)

elif page == "FAQs":
    st.header("📋 Frequently Asked Questions")
    for question, answer in faq.items():
        with st.expander(f"**❓ {question}**"):
            st.write(answer)

    # Additional FAQs for System Instructions & Configurations
    st.header("🔧 AI FAQs")
    
    faqs_system = {
       " How can I use this bot for stress relief?":"You can use this bot to get personalized stress management tips, relaxation exercises, and AI-generated advice. Simply enter your stress-related concern in the input field, and the AI will provide helpful suggestions.",
       "Can this bot help with serious mental health issues?":"This bot provides general stress relief tips and mental well-being advice, but it does not replace professional therapy. If you're experiencing severe distress, it's best to consult a licensed mental health professional.",
       "What types of questions can I ask this bot?":"You can ask about stress management tips, relaxation exercises, mindfulness techniques, and ways to handle anxiety or burnout. However, it does not provide medical diagnoses or crisis support."
        }

    for question, answer in faqs_system.items():
        with st.expander(f"**🔍 {question}**"):
            st.write(answer)
