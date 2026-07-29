import streamlit as st
import pandas as pd
import joblib


# Load Model & Columns file
model = joblib.load("model.pkl")
training_columns = joblib.load("columns.pkl")


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer will leave or stay at the company.")

st.markdown("---")


# User Inputs
gender = st.selectbox("Gender", ["Female", "Male"])

SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

InternetService = st.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    [
        "No",
        "Yes"
    ]
)

Contract = st.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)


# Create DataFrame
input_df = pd.DataFrame({

    "gender":[gender],
    "SeniorCitizen":[SeniorCitizen],
    "tenure":[tenure],
    "InternetService":[InternetService],
    "OnlineSecurity":[OnlineSecurity],
    "Contract":[Contract],
    "PaymentMethod":[PaymentMethod],
    "MonthlyCharges":[MonthlyCharges],
    "TotalCharges":[TotalCharges]

})

# One Hot Encoding
input_df = pd.get_dummies(
    input_df,
    drop_first=True
)

# Match Training Columns
input_df = input_df.reindex(
    columns=training_columns,
    fill_value=0
)

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.markdown("---")

    if prediction == 1:
        st.error("⚠ Customer is likely to Leave")
    else:
        st.success("✅ Customer is likely to Stay")

    st.subheader("Prediction Probability")

    st.write(f"Stay : **{probability[0]*100:.2f}%**")
    st.write(f"Leave : **{probability[1]*100:.2f}%**")