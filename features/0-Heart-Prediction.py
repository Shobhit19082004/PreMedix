import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the trained model
with open('heart_disease_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to make predictions
def predict_heart_failure(features):
    prediction = model.predict([features])
    return prediction

# Streamlit app
def main():
    st.title("Heart Failure Prediction")
    st.markdown("""
    This app predicts whether a patient will experience heart failure based on their medical data.
    """)

    # Input fields for the features
    age = st.number_input("Age", min_value=0, max_value=120, value=50)
    anaemia = st.selectbox("Anaemia", ["No", "Yes"])
    high_blood_pressure = st.selectbox("High Blood Pressure", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase (CPK)", min_value=0, value=100)
    ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=0, max_value=100, value=60)
    serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0, value=1.0)
    serum_sodium = st.number_input("Serum Sodium", min_value=100, max_value=150, value=140)
    platelets = st.number_input("Platelets", min_value=100000, value=200000)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    rest_ecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    st_depression = st.number_input("ST Depression Induced by Exercise", min_value=0.0, value=0.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    num_vessels = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", ["0", "1", "2", "3"])
    thalassemia = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    # Convert categorical features to numerical
    anaemia = 1 if anaemia == "Yes" else 0
    high_blood_pressure = 1 if high_blood_pressure == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0
    smoking = 1 if smoking == "Yes" else 0
    sex = 1 if sex == "Male" else 0
    chest_pain_type = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(chest_pain_type)
    fasting_blood_sugar = 1 if fasting_blood_sugar == "Yes" else 0
    rest_ecg = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(rest_ecg)
    exercise_angina = 1 if exercise_angina == "Yes" else 0
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
    num_vessels = int(num_vessels)
    thalassemia = ["Normal", "Fixed Defect", "Reversible Defect"].index(thalassemia)

    # Prepare the features for prediction
    features = np.array([age, anaemia, high_blood_pressure, diabetes, smoking, creatinine_phosphokinase, ejection_fraction,
                         serum_creatinine, serum_sodium, platelets, sex, chest_pain_type, fasting_blood_sugar, rest_ecg,
                         exercise_angina, st_depression, slope, num_vessels, thalassemia])

    if st.button("Predict"):
        result = predict_heart_failure(features)
        if result == 1:
            st.write("The patient is at risk of heart failure.")
        else:
            st.write("The patient is not at risk of heart failure.")
