import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import json
from features.auth import authentication

# Set Page Configuration
st.set_page_config(page_title="🩺 PreMedix - Disease Prediction System", layout="wide")

# Initialize session state keys
if 'register' not in st.session_state:
    st.session_state['register'] = False
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}

# Initialize the authentication object
authentication()

if st.session_state["authentication_status"]:
     pg = st.navigation([
         st.Page("features/inro.py", title="Home", icon="🏠"),
         st.Page("features/0-Heart-Prediction.py", title="Heart Disease Prediction", icon="❤️"),
         st.Page("features/1-Lung-cancer.py", title="Lung Cancer Prediction", icon="🦠"),
         st.Page("features/2-Brain-Stroke-Prediction.py", title="Brain Stroke Prediction", icon="🧠"),
         st.Page("features/3-Diabetes-Prediction.py", title="Diabetes Prediction", icon="🍥"),
         st.Page("features/4-Breast-Cancer-Prediction", title="Breast Cancer Prediction", icon="👨‍⚕️"),
         st.Page("features/5-Symptom-Checker.py",title="Symptom Checker AI", icon="🤒"),
         st.Page("features/6-Medical Image Analysis.py",title="Medical Image Assistant", icon="🩻"),
         st.Page("features/7-DietplanAI.py",title="AI Diet Planner", icon="🍽️"),
     ])
     pg.run()