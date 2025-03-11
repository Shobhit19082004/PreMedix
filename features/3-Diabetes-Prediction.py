import streamlit as st
import pandas as pd
import pickle

# Load the SVC model
def load_model():
    with open("features/rfc_pickle.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# HTML and CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f7f7f7;
        }
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            color: #FF6F61;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .description {
            text-align: center;
            font-size: 1.2rem;
            color: #555;
            margin-bottom: 30px;
        }
        .prediction-section {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .btn-predict {
            background-color: #FF6F61;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1rem;
            cursor: pointer;
            border-radius: 5px;
        }
        .btn-predict:hover {
            background-color: #e65a54;
        }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.markdown('<h1 class="main-title">🩺 Diabetes Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Provide your health details below to get a prediction on your diabetes risk.</p>', unsafe_allow_html=True)

# Sidebar for input descriptions
st.sidebar.title("📝 Input Descriptions")
st.sidebar.write("""
- **Pregnancies:** Number of times pregnant.  
- **Glucose Level:** Higher glucose levels indicate higher risk.  
- **Blood Pressure:** Diastolic blood pressure (mm Hg).  
- **Skin Thickness:** Triceps skinfold thickness (mm).  
- **Insulin Level:** 2-hour serum insulin (mu U/ml).  
- **BMI:** Body mass index, weight in kg/(height in m)^2.  
- **Diabetes Pedigree Function:** Likelihood of diabetes based on family history.  
- **Age:** Age in years.  
""")

# Collect user inputs
st.markdown('<div class="prediction-section">', unsafe_allow_html=True)

pregnancies = st.number_input("Number of Pregnancies:", min_value=0, max_value=20, value=0)
glucose = st.slider("Glucose Level (mg/dL):", 50, 200, 100)
blood_pressure = st.slider("Blood Pressure (mm Hg):", 40, 140, 80)
skin_thickness = st.slider("Skin Thickness (mm):", 0, 100, 20)
insulin = st.slider("Insulin Level (mu U/ml):", 0, 500, 50)
bmi = st.slider("Body Mass Index (BMI):", 10.0, 50.0, 25.0, step=0.1)
dpf = st.slider("Diabetes Pedigree Function:", 0.0, 2.5, 0.5, step=0.01)
age = st.number_input("Age (years):", min_value=10, max_value=100, value=25)

st.markdown('</div>', unsafe_allow_html=True)

# Prepare input data for prediction
input_data = pd.DataFrame({
    "Pregnancies": [pregnancies],
    "Glucose": [glucose],
    "BloodPressure": [blood_pressure],
    "SkinThickness": [skin_thickness],
    "Insulin": [insulin],
    "BMI": [bmi],
    "DiabetesPedigreeFunction": [dpf],
    "Age": [age]
})

# Prediction button
if st.button("🧮 Predict", help="Click to analyze your diabetes risk."):
    prediction = model.predict(input_data)

    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("⚠️ The model predicts that you are at risk of diabetes. Please consult a healthcare professional.")
    else:
        st.success("✅ The model predicts that you are not at risk of diabetes.")
