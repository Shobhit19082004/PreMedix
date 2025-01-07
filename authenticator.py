import os
import time
import csv
import yaml
import json
from PIL import Image
import pandas as pd
import numpy as np
import streamlit as st
import streamlit_lottie as st_lottie
import matplotlib.pyplot as plt
import seaborn as sns
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import LoginError
from streamlit_authenticator.utilities.hasher import Hasher
from streamlit_gsheets import GSheetsConnection
from ydata_profiling import ProfileReport
import google.generativeai as genai
from dotenv import load_dotenv
from sklearn.impute import SimpleImputer

# conn = st.connection("gsheets", type=GSheetsConnection)
# # Read the data from Google Sheets
# feedback_df = conn.read(worksheet="Feedback Data", ttl=60)
# query_df = conn.read(worksheet="Query Data", ttl=60)
# user_df = conn.read(worksheet="UserLogin", ttl=60)
# Loading config file
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize session state for register page
if 'register' not in st.session_state:
    st.session_state['register'] = False

def show_login_form():
    # Creating the authenticator object
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        # config['register_user']
    )
    
    # Creating a login widget
    try:
        authenticator.login()
    except LoginError as e:
        st.error(e)
    
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout',"sidebar")
        st.sidebar.write(f'Welcome **{st.session_state["name"]}**👋')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    # Only show the "Register" button if the user is NOT logged in
    if st.session_state["authentication_status"] is None or st.session_state["authentication_status"] == False:
        st.write("---")
        if st.button("Register"):
            st.session_state['register'] = True  # Switch to register page

# Define function to show the register form
def show_register_form():
    st.write("## Register")
    new_username = st.text_input("Enter a new username")
    new_name = st.text_input("Enter your full name")
    new_password = st.text_input("Enter a new password", type="password")
    new_email = st.text_input("Enter your email")

    if st.button("Submit Registration"):
        if new_username and new_password and new_email:
            # Hash the new password
            # hashed_password = Hasher().generate(new_password)[0]
            hashed_password = Hasher([new_password]).hash(new_password)
            if 'credentials' not in config:
                config['credentials'] = {}
            if 'usernames' not in config['credentials']:
                config['credentials']['usernames'] = {}
                
             # Update the config dictionary
            config['credentials']['usernames'][new_username] = {
                'name': new_name,
                'password': hashed_password,
                'email': new_email
            }
        
            # Save the updated credentials to the config.yaml file
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file)
                
            # #user_data = pd.DataFrame({
            #                 "Username": new_username,
            #                 "Name": new_name,
            #                 "Email": new_email,
            #                 "Hash_pass": hashed_password
            #             }, index=[0])
                    
            # # Update the user data
            # updated_df = pd.concat([user_df, user_data], ignore_index=True)

            # # Update Google Sheets with new User Data
            # conn.update(worksheet="UserLogin", data=updated_df)
            # st.success("User registered successfully! You can now log in.")
            st.session_state['register'] = False  # Go back to login page
        else:
            st.error("Please fill out all fields")

    # Add a "Back to Login" button to return to the login page
    if st.button("Back to Login"):
        st.session_state['register'] = False  # Return to login page

# Main section: Show either login or register form based on state
if st.session_state['register']:
    show_register_form()  # Show register form
else:
    show_login_form()  # Show login form