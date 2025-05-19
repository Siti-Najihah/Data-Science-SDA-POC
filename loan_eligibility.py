import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load the trained model and feature columns
model = joblib.load(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\50k datasets\loan_eligibility_model.pkl")
model_features = joblib.load(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\50k datasets\model_features.pkl")

# Streamlit app
st.title("Loan Eligibility Prediction")

# Input fields for user data
st.header("Enter Business Details")

business_age = st.number_input("Business Age (years)", min_value=1, max_value=50, value=5)
annual_revenue = st.number_input("Annual Revenue (RM)", min_value=50000, max_value=50000000, value=1000000)
existing_loan = st.selectbox("Existing Loan", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
profit_margin = st.number_input("Profit Margin (%)", min_value=5, max_value=30, value=15)
loan_amount_requested = st.number_input("Loan Amount Requested (RM)", min_value=10000, max_value=500000, value=250000)
industry = st.selectbox("Industry", ['Manufacturing', 'Services', 'Agriculture', 'Construction', 'Retail'])
location = st.selectbox("Location", [
    'Johor', 'Kedah', 'Kelantan', 'Malacca', 'Negeri Sembilan', 
    'Pahang', 'Penang', 'Perak', 'Perlis', 'Sabah', 
    'Sarawak', 'Selangor', 'Terengganu', 'Kuala Lumpur'
])

# Prepare the input data for prediction
input_data = {
    "Business Age (years)": business_age,
    "Annual Revenue (RM)": annual_revenue,
    "Existing Loan": existing_loan,
    "Credit Score": credit_score,
    "Profit Margin (%)": profit_margin,
    "Loan Amount Requested (RM)": loan_amount_requested,
    "Industry": industry,
    "Location": location
}

# Convert input_data to a DataFrame
input_df = pd.DataFrame([input_data], columns=model_features)  # Ensure columns match the model's expected features

# Predict loan eligibility
if st.button("Predict Loan Eligibility"):
    try:
        # Get the probability of being eligible (class 1)
        score_percentage = model.predict_proba(input_df)[0][1] * 100  

        # Add slight randomness to make the feedback more natural
        adjusted_score = score_percentage + np.random.uniform(-2, 2)  # Add a small random adjustment
        adjusted_score = max(0, min(100, adjusted_score))  # Ensure the score stays within 0-100%

        # Provide feedback based on the adjusted score percentage
        if adjusted_score >= 80:
            feedback = (
                "High Eligibility: The business demonstrates strong financial health and meets most criteria for loan approval."
            )
        elif adjusted_score >= 60:
            feedback = (
                "Good Eligibility: The business has a good chance of loan approval, but some factors may require further review."
            )
        elif adjusted_score >= 40:
            feedback = (
                "Moderate Eligibility: The business may qualify for a loan, but there are notable areas of concern."
            )
        elif adjusted_score >= 20:
            feedback = (
                "Low Eligibility: The business has significant challenges that may hinder loan approval."
            )
        else:
            feedback = (
                "Very Low Eligibility: The business does not meet the minimum criteria for loan approval."
            )

        # Display results
        prediction = model.predict(input_df)[0]  # Predict eligibility (0 or 1)
        if prediction == 1:
            st.success(
                f"The business is eligible for the loan. Probability of eligibility: {adjusted_score:.2f}%"
            )
        else:
            st.error(
                f"The business is not eligible for the loan. Probability of eligibility: {adjusted_score:.2f}%"
            )

        # Display detailed feedback
        st.info(feedback)


    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")