import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load Models
models = {
    "Heart Disease": "features/heart_disease_model.pkl",
    #"Lung Cancer": "lung_cancer_model.pkl",
    "Diabetes": "features/rfc_pickle.pkl",
    #"Brain Stroke": "brain_stroke_model.pkl",
    #"Breast Cancer": "breast_cancer_model.pkl"
}

loaded_models = {}
for name, file in models.items():
    with open(file, "rb") as f:
        loaded_models[name] = pickle.load(f)

# Sidebar Navigation
st.sidebar.title("🔍 PreMedix - Multi-Disease Prediction")
selected_model = st.sidebar.radio("Choose a Disease Prediction Model:", list(models.keys()))

# App Title
st.title(f"🩺 {selected_model} Prediction")
st.write("Enter the required details below to get a prediction.")

# Function to make predictions
def predict(model, user_input):
    user_input = np.array([user_input])  # Reshape for model
    prediction = model.predict(user_input)[0]
    return prediction

# Input Forms Based on Selected Model
if selected_model == "Heart Disease":
    # st.subheader("❤️ Heart Disease Prediction")
    # age = st.number_input("Age", min_value=1, max_value=120, value=25)
    # sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    # cp = st.selectbox("Chest Pain Type (CP)", [0, 1, 2, 3])
    # trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
    # chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=100, max_value=500, value=200)
    # user_input = [age, sex, cp, trestbps, chol
    st.warning('⚠️Note: This Heart Disease prediction is powered by Machine Learning from PreMedix. Please use the results responsibly and seek professional medical advice if needed.')

st.header('❤️ Heart Disease Prediction App', anchor='heart-disease-prediction', divider='rainbow')
with st.expander('What is Heart Disease Prediction App?'):
    st.write('The Heart Disease Prediction App is a Machine Learning based simple and user-friendly tool designed to help you assess your risk of heart disease. By entering basic health details like your age, cholesterol levels, and blood pressure, the app provides an instant prediction based on advanced technology. It is easy to use, visually appealing, and helps you stay informed about your heart health.')
    # Symptom Details
st.write("Please provide your health details below to get a prediction on your heart disease risk.") 
# Sidebar for input descriptions
st.sidebar.title("📝 Input Descriptions")
st.sidebar.write("""
- **Age:** Enter your age in years. Risk increases with age.  
- **Gender:** Males generally have a higher risk.  
- **Chest Pain Type:** Different types can indicate varying levels of risk:
  - *Typical Angina*: Predictable chest pain during exertion.
  - *Atypical Angina*: Unpredictable chest discomfort.
  - *Non-anginal Pain*: Not heart-related pain.
  - *Asymptomatic*: No chest pain symptoms.  
 - **Resting Blood Pressure:** High levels (>120 mmHg) indicate hypertension.  
 - **Cholesterol Level:** A cholesterol level above 200 mg/dL is considered high.  
 - **Fasting Blood Sugar:** High fasting sugar levels (>120 mg/dL) may indicate diabetes.  
 - **Resting ECG Results:** Indicates heart electrical activity.
 - **Max Heart Rate Achieved:** Lower values could indicate heart problems.  
 - **Exercise-Induced Angina:** Chest pain due to reduced heart blood flow during exercise.  
""")

 # Collect user inputs
 # st.markdown('<div class="prediction-section">', unsafe_allow_html=True)

age = st.number_input("Age (years):", min_value=18, max_value=100, value=50)
sex = st.radio("Gender:", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type:", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.slider("Resting Blood Pressure (mm Hg):", 80, 200, 120)
chol = st.slider("Cholesterol Level (mg/dL):", 100, 400, 200)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dL:", ["No", "Yes"])
restecg = st.selectbox("Resting ECG Results:", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
thalach = st.slider("Maximum Heart Rate Achieved:", 60, 220, 150)
exang = st.radio("Exercise-Induced Angina:", ["No", "Yes"])
oldpeak = st.slider("ST Depression (mm):", 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment:", ["Upsloping", "Flat", "Downsloping"])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy:", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia Type:", ["Normal", "Fixed Defect", "Reversible Defect"])
smoking = st.radio("Do you smoke?", ["No", "Yes"])
alcohol = st.radio("Do you consume alcohol?", ["No", "Yes"])

st.markdown('</div>', unsafe_allow_html=True)

# Map user inputs to numerical values
sex_mapping = {"Male": 1, "Female": 0}
cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
fbs_mapping = {"No": 0, "Yes": 1}
restecg_mapping = {"Normal": 0, "ST-T Wave Abnormality": 1, "Left Ventricular Hypertrophy": 2}
exang_mapping = {"No": 0, "Yes": 1}
slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
thal_mapping = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
smoking_mapping = {"No": 0, "Yes": 1}
alcohol_mapping = {"No": 0, "Yes": 1}

# Prepare input data for prediction
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex_mapping[sex]],
    "cp": [cp_mapping[cp]],
    "trestbps": [trestbps],
    "chol": [chol],
    "fbs": [fbs_mapping[fbs]],
    "restecg": [restecg_mapping[restecg]],
    "thalach": [thalach],
    "exang": [exang_mapping[exang]],
    "oldpeak": [oldpeak],
    "slope": [slope_mapping[slope]],
    "ca": [ca],
    "thal": [thal_mapping[thal]],
    "smoking": [smoking_mapping[smoking]],
    "alcohol": [alcohol_mapping[alcohol]]
})

# Prediction button
if st.button("🧮 Predict", help="Click to analyze your heart disease risk."):
    prediction = selected_model.predict(input_data)
    prediction_proba = selected_model.predict_proba(input_data)

    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("⚠️ The model predicts that you are at risk of heart disease. Please consult a healthcare professional.")
    else:
        st.success("✅ The model predicts that you are not at risk of heart disease.")

    st.subheader("Prediction Probability:")
    st.write(f"Risk of Heart Disease: {prediction_proba[0][1] * 100:.2f}%")
    st.write(f"No Risk: {prediction_proba[0][0] * 100:.2f}%")

# elif selected_model == "Lung Cancer":
#     st.subheader("🫁 Lung Cancer Prediction")
#     age = st.number_input("Age", min_value=1, max_value=120, value=25)
#     smoking = st.selectbox("Smoking Habit", [0, 1])
#     wheezing = st.selectbox("Wheezing", [0, 1])
#     chest_pain = st.selectbox("Chest Pain", [0, 1])
#     user_input = [age, smoking, wheezing, chest_pain]

elif selected_model == "Diabetes":
    st.subheader("💉 Diabetes Prediction")
    glucose = st.number_input("Glucose Level", min_value=50, max_value=200, value=100)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    user_input = [glucose, bmi]

# elif selected_model == "Brain Stroke":
#     st.subheader("🧠 Brain Stroke Prediction")
#     age = st.number_input("Age", min_value=1, max_value=120, value=25)
#     hypertension = st.selectbox("Hypertension", [0, 1])
#     user_input = [age, hypertension]

# elif selected_model == "Breast Cancer":
#     st.subheader("🎗️ Breast Cancer Prediction")
#     radius_mean = st.number_input("Mean Radius", min_value=0.0, max_value=50.0, value=14.0)
#     user_input = [radius_mean]

# Predict Button
if st.button("Predict"):
    prediction = predict(loaded_models[selected_model], user_input)
    if prediction == 1:
        st.error("⚠️ High Risk Detected! Please consult a doctor.")
    else:
        st.success("✅ No Risk Detected! Maintain a healthy lifestyle.")
