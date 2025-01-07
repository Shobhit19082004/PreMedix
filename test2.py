import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import json

# Set Page Configuration
st.set_page_config(page_title="PreMedix - Disease Prediction System", layout="wide")

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
image = Image.open('banner.jpg')  # Replace 'banner.jpg' with your image
st.image(image, use_column_width=True)

# Title and Introduction
st.markdown("""
<h1 style='text-align: center; font-size: 60px; color:#4A90E2; font-family: Arial Black;'>🩺 PreMedix</h1>
<h3 style='text-align: center; font-size: 28px; color:#7F8C8D;'>Empowering Health with AI-driven Predictions</h3>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# About PreMedix Section
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <h2 style='color:#27AE60; font-size: 32px;'>ℹ️ About PreMedix</h2>
    <p style='font-size: 18px; line-height: 1.8;'>
    '''<b>PreMedix</b> is a cutting-edge, AI-powered web application designed to <b>detect multiple diseases</b> with high accuracy.<br>
    -It uses advanced machine learning and deep learning algorithms to analyze user inputs and predict disease likelihood quickly and efficiently.'''
    </p>
    """, unsafe_allow_html=True)

with col2:
    path = get('Animation - 1736172441933.json')
    st_lottie(path, height=250)

st.markdown("<br><br>", unsafe_allow_html=True)

# Features Section
col1, col2 = st.columns([1, 1])

with col2:
    st.markdown("""
    <h2 style='color:#E67E22; font-size: 32px;'>✨ Key Features</h2>
    <ul style='font-size: 18px; line-height: 2;'>
    <li><b>🔍 Multi-Disease Detection:</b> Supports predictions for:</li>
    <ul>
    <li>🫁 Lung Cancer</li>
    <li>❤️ Heart Disease</li>
    <li>🖼️ Skin Cancer</li>
    <li>💉 Diabetes</li>
    <li>🧠 Brain Tumor</li>
    <li>🦟 Malaria</li>
    <li>🦠 Dengue</li>
    <li>👨‍🦯 Parkinson's Disease</li>
    </ul>
    <li><b>🖥️ User-Friendly Interface:</b> Interactive and easy-to-use design.</li>
    <li><b>⚡ AI-Powered Accuracy:</b> Ensures high prediction performance.</li>
    <li><b>🔒 Secure and Private:</b> Data is processed securely without storage.</li>
    </ul>
    """, unsafe_allow_html=True)

with col1:
    path = get('Animation - 1736184853531.json')
    st_lottie(path, height=300)

st.markdown("<br><br>", unsafe_allow_html=True)

# Benefits Section
col3, col4 = st.columns([1, 1])

with col3:
    st.markdown("""
    <h2 style='color:#8E44AD; font-size: 32px;'>🌟 Why Choose PreMedix?</h2>
    <ul style='font-size: 18px; line-height: 2;'>
    <li><b>⏳ Early Detection Saves Lives:</b> Timely predictions can lead to faster treatments and better outcomes.</li>
    <li><b>📱 Accessible Anywhere:</b> Available on any device with an internet connection.</li>
    <li><b>👌 Easy to Use:</b> No technical knowledge required—just input data and get results!</li>
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
