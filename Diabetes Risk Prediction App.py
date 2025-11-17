import streamlit as st
import pandas as pd
import pickle

# Opening the Saved Predictive Model
@st.cache_resource
def load_model():
    with open("Final_RandomForest_Model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

RandomForest_Model = load_model()

# -----------------------------
# Page Title
# -----------------------------
st.title("🩺 Diabetes Risk Prediction App")
st.write("Enter patient health details below to predict diabetes risk using a trained Supervised Model.")

# -----------------------------
# User Input Form
# -----------------------------
st.subheader("Enter Patient Details:")

# Input fields
Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
Glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)
BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
Insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
BMI = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
Age = st.number_input("Age", min_value=1, max_value=120, value=30)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Diabetes Risk"):
    # Create input dataframe
    input_data = pd.DataFrame({
        "Pregnancies": [Pregnancies],
        "Glucose": [Glucose],
        "BloodPressure": [BloodPressure],
        "SkinThickness": [SkinThickness],
        "Insulin": [Insulin],
        "BMI": [BMI],
        "DiabetesPedigreeFunction": [DiabetesPedigreeFunction],
        "Age": [Age]
    })

    # Make prediction
    prediction = RandomForest_Model.predict(input_data)[0]
    prediction_proba = RandomForest_Model.predict_proba(input_data)[0][1]

    # Display result
    if prediction == 1:
        st.error(f"⚠️ The model predicts that the person **is likely diabetic.**")
    else:
        st.success(f"✅ The model predicts that the person **is not diabetic.**")

    st.write(f"**Predicted Probability of Diabetes:** {prediction_proba:.2f}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Model: Random Forest Classifier | Created by Naveen Gupta")
