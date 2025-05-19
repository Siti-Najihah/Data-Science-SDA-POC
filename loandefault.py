import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and LabelEncoder
model = joblib.load(r'C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\din\MIA\loan_default_model.pkl')
le = joblib.load(r'C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\din\MIA\label_encoder.pkl')

st.title("Loan Default Prediction App")

st.sidebar.header("Input Features")

# User inputs
arrears_pattern = st.sidebar.selectbox(
    "Monthly Arrears Pattern",
    options=[0, 1, 2, 3],
    format_func=lambda x: {
        0: "No missed payments",
        1: "1 month missed payment",
        2: "2 months missed payments",
        3: "2 or more consecutive months missed payments"
    }[x]
)

loan_amount = st.sidebar.number_input("Loan Amount", min_value=1000, max_value=100000000, value=50000, step=1000)
existing_loans = st.sidebar.slider("Number of Existing Loans", 0, 10, 2)
interest_rate = st.sidebar.slider("Interest Rate (%)", 0.0, 20.0, 5.0, step=0.1)
loan_length = st.sidebar.slider("Loan Length (months)", 6, 360, 60)
profit_margin = st.sidebar.slider("Profit Margin (%)", 0.0, 100.0, 10.0, step=0.1)
company_sector = st.sidebar.selectbox("Company Sector", le.classes_)

# Encode 'Company Sector' using the loaded LabelEncoder
company_sector_encoded = le.transform([company_sector])[0]

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Monthly Arrears Pattern': [arrears_pattern],
    'Loan Amount': [loan_amount],
    'Existing Loans': [existing_loans],
    'Interest Rate': [interest_rate],
    'Loan Length': [loan_length],
    'Profit Margin': [profit_margin / 100],  # Convert percentage to decimal
    'Company Sector': [company_sector_encoded]
})

# Ensure the input_data columns are in the same order as the training data
expected_features = ['Monthly Arrears Pattern', 'Loan Amount', 'Existing Loans',
                     'Interest Rate', 'Loan Length', 'Profit Margin', 'Company Sector']
input_data = input_data[expected_features]

# Make prediction
default_probability = model.predict_proba(input_data)[0][1]
prediction = model.predict(input_data)[0]

# Function to categorize risk based on probability
def categorize_risk(prob):
    if prob >= 0.80:
        return "Highly likely to default", "red"
    elif prob >= 0.60:
        return "Likely to default", "orange"
    elif prob >= 0.30:
        return "Possible to default", "violet"
    else:
        return "Least likely to default", "green"

risk_category, color = categorize_risk(default_probability)

# Display prediction results
st.subheader("Prediction Results")
st.write(f"**Default Probability:** {default_probability:.2%}")
st.markdown(f"**Risk Category:** :{color}[{risk_category}]")
