import numpy as np
import pandas as pd
import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load("LinearRegression.pkl")

LR_model = load_model()

st.title("Insurance Cost Prediction")
st.write("Enter the details below to predict insurance charges.")

# Sidebar Input
st.sidebar.header("Patient Details")

age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.sidebar.radio("Sex", options=["Male", "Female"])
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.sidebar.slider("Number of Children", 0, 5, 0)
smoker = st.sidebar.radio("Smoker", options=["Yes", "No"])
region = st.sidebar.selectbox("Region", ["Southeast", "Southwest", "Northeast", "Northwest"])

sex = 0 if sex == "Male" else 1
smoker = 0 if smoker == "Yes" else 1
region_dict = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}
region = region_dict[region]

# Prediction
input_data = np.array([[age, sex, bmi, children, smoker, region]])
prediction = LR_model.predict(input_data)

# Display Result
st.subheader("Predicted Insurance Cost 💰")
st.write(f"**Estimated Charges: USD {prediction[0]:,.2f}**")

# Add Dataset Preview Option
if st.checkbox("Show Sample Data"):
    df = pd.read_csv("insurance.csv")
    st.write(df.head(10))
