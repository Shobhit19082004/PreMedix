import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import json
from features.auth import authentication


# Function to Load Lottie Animations
def get(path: str):
    with open(path) as p:
        return json.load(p)

# CSS for font styles
st.markdown("""
    <style>
        /* Importing Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f4f4;
        }

        h1, h2, h3 {
            font-family: 'Poppins', sans-serif;
        }

        h1 {
            font-size: 60px;
            color: #4A90E2;
            text-align: center;
            font-weight: 600;
        }

        h3 {
            font-size: 28px;
            color: #7F8C8D;
            text-align: center;
            font-weight: 400;
        }

        h2 {
            font-size: 32px;
            color: #27AE60;
            font-weight: 600;
        }

        p {
            font-size: 18px;
            line-height: 1.8;
            font-weight: 400;
        }

        ul {
            font-size: 18px;
            line-height: 2;
            font-weight: 400;
        }

        li {
            margin-bottom: 10px;
        }

        a {
            color: #3498DB;
        }

        .footer {
            text-align: center;
            font-size: 16px;
            color: #7F8C8D;
        }
    </style>
""", unsafe_allow_html=True)


# Banner Image 
image = Image.open('Banner3.jpg')  

import base64
from io import BytesIO

buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{img_str}" style="width: 1200px; height: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(59, 13, 175, 0.2);"/>
    </div>
""", unsafe_allow_html=True)

# # Banner Image
# image = Image.open('banner.jpg')  
# image = image.resize((800, 200))  
# st.image(image, use_column_width=False)
#Empowering Health with AI-driven Predictions
# Title and Introduction
st.markdown("""
<h1 style='text-align: center; font-size: 60px; color:#4A90E2; font-family: Arial Black;'> 🧑🏽‍⚕️PreMedix</h1>
<h3 style='text-align: center; font-size: 28px; color:#7F8C8D;'>Empowering Healthcare with AI: Precise Predictions, Better Lives
</h3>
<style>
#   h1 {
#     border-bottom: 4px solid;
#     border-image: linear-gradient(to right, #FF7F50, #FFD700, #32CD32, #1E90FF);
#     border-image-slice: 1;
  }
  h3 {
    border-bottom: 4px solid;
    border-image: linear-gradient(to right, #FF7F50, #FFD700, #32CD32, #1E90FF);
    border-image-slice: 1;
  }
</style>
""", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)

# About PreMedix Section
col1, col2 = st.columns([1, 1])

with col1:
    st.header("ℹ️ About PreMedix",divider="rainbow")
    st.markdown("""<p style='font-size: 20px; line-height: 1.8;'>
    <b>PreMedix</b> is a cutting-edge, AI-powered web application designed to <b>detect multiple diseases</b> with high accuracy.<br>
        <ul style='list-style-type: none; padding: 0;'>
        <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'>🌟 PreMedix is an AI-powered web application designed to predict multiple diseases quickly and accurately. Using advanced machine learning algorithms, it simplifies healthcare by providing fast, reliable, and secure predictions. With a user-friendly interface and smart analytics, PreMedix helps users make informed health decisions, enabling early diagnosis and better outcomes—all from the comfort of their devices.</li>
        <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'>🌟 It uses advanced machine learning and deep learning algorithms to analyze user inputs and predict disease likelihood quickly and efficiently.</li>
        </ul>
    </p>
    """, unsafe_allow_html=True)
    

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    path = get('Animation - 1736172441933.json')
    st_lottie(path, height=300)

st.markdown("<br><br>", unsafe_allow_html=True)

# Features Section
col1, col2 = st.columns([1, 1])

with col2:
    st.header("✨ Key Features", divider="rainbow")
    st.markdown("""
    <ul style='font-size: 18px; line-height: 2; list-style-type: none; padding: 0;'>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>🔍 Machine Learning Based Multi-Disease Detection:</b></li>
    </ul>
    <ul style='list-style-type: none; padding: 0;'>
    <li >🫁 Lung Cancer</li>
    <li >❤️ Heart Disease</li>
    <li >🖼️ Skin Cancer</li>
    <li >💉 Diabetes</li>
    <li >🧠 Brain Tumor</li>
    <li >🦟 Malaria</li>
    <li >🦠 Dengue</li>
    <li >👨‍🦯 Parkinson's Disease</li>
    </ul>
    <ul style='list-style-type: none; padding: 0;'>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>🖥️ User-Friendly Interface:</b> Interactive and easy-to-use design.</li>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>⚡ AI-Powered Accuracy:</b> Ensures high prediction performance.</li>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>🔒 Secure and Private:</b> Data is processed securely without storage.</li>
    </ul>
    """, unsafe_allow_html=True)

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    path = get('Animation - 1736184853531.json')
    st_lottie(path, height=400)

st.markdown("<br><br>", unsafe_allow_html=True)

# Benefits Section
col3, col4 = st.columns([1, 1])

with col3:
    st.header("🌟 Why Choose PreMedix?",divider="rainbow")
    st.markdown("""
    <ul style='font-size: 18px; line-height: 2;'>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>⏳ Early Detection Saves Lives:</b> Timely predictions can lead to faster treatments and better outcomes.</li>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>📱 Accessible Anywhere:</b> Available on any device with an internet connection.</li>
    <li style='margin: 5px 0; padding: 10px; border-radius: 5px;'><b>👌 Easy to Use:</b> No technical knowledge required—just input data and get results!</li>
    </ul>
    """, unsafe_allow_html=True)

with col4:
    path = get('Animation - 1736172774697.json')
    st_lottie(path, height=300)

st.markdown("<br><br>", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<h2 style='color:#3498DB; font-size: 32px;'>📞 Contact Us</h2>
<p style='font-size: 18px;'>
- <b>Email:</b> support@premedix.com<br>
- <b>Phone:</b> +91 123-456-7890<br>
- <b>Website:</b> <a href='http://www.premedix.com' style='color:#E74C3C;'>www.premedix.com</a>
</p>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='color:#F39C12; font-size: 32px;'>📢 Stay Connected!</h2>
<p style='font-size: 18px;'>
Follow us on 
<a href='https://www.linkedin.com' style='color:#3498DB;'>LinkedIn</a> | 
<a href='https://www.twitter.com' style='color:#3498DB;'>Twitter</a> | 
<a href='https://www.instagram.com' style='color:#3498DB;'>Instagram</a>
</p>
""", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color:#7F8C8D;'>© 2025 PreMedix. All Rights Reserved.</p>", unsafe_allow_html=True)