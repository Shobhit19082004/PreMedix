import streamlit as st
import pandas as pd
import pickle

# Sidebar Navigation
st.sidebar.title("MultiPredict")
page = st.sidebar.radio("Navigate", ["Heart Disease prediction", "Lung Cancer Prediction", "Brain Stroke Prediction", "Diabetes Prediction", "Breast Cancer Prediction" ])

# Load the trained model
############################################ Heaart Disease Prediction ##################################################################################################################################################################################################################################################################################################################
if page == "Heart Disease prediction":
 def load_model():
    with open("features/heart_disease_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model
 model = load_model()

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
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("⚠️ The model predicts that you are at risk of heart disease. Please consult a healthcare professional.")
    else:
        st.success("✅ The model predicts that you are not at risk of heart disease.")

    st.subheader("Prediction Probability:")
    st.write(f"Risk of Heart Disease: {prediction_proba[0][1] * 100:.2f}%")
    st.write(f"No Risk: {prediction_proba[0][0] * 100:.2f}%")
