import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

# Define all possible labels for Industry, Location, and SME Category
all_possible_industries = ['Manufacturing', 'Services', 'Agriculture', 'Construction', 'Retail']
all_possible_locations = [
    'Johor', 'Kedah', 'Kelantan', 'Malacca', 'Negeri Sembilan', 
    'Pahang', 'Penang', 'Perak', 'Perlis', 'Sabah', 
    'Sarawak', 'Selangor', 'Terengganu', 'Kuala Lumpur'
]
all_possible_categories = ['Micro', 'Small', 'Medium', 'Large']

# Fit LabelEncoders with all possible labels
label_encoder_industry = LabelEncoder()
label_encoder_industry.fit(all_possible_industries)
joblib.dump(label_encoder_industry, r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\label_encoder_industry.pkl")

label_encoder_location = LabelEncoder()
label_encoder_location.fit(all_possible_locations)
joblib.dump(label_encoder_location, r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\label_encoder_location.pkl")

label_encoder_category = LabelEncoder()
label_encoder_category.fit(all_possible_categories)
joblib.dump(label_encoder_category, r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\label_encoder_category.pkl")

# Load the trained model
model = joblib.load(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\sme_loan_model.pkl")

# Load the LabelEncoder for categorical features
label_encoder_industry = joblib.load(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\label_encoder_industry.pkl")
label_encoder_location = joblib.load(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\label_encoder_location.pkl")
label_encoder_category = joblib.load(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\harith\Test\label_encoder_category.pkl")

# Streamlit app title
st.title("SME Loan Eligibility Amount Predictor")

# Input fields for user data
st.header("Enter Your Business Details")
business_age = st.number_input("Business Age (years)", min_value=1, max_value=50, value=5)
annual_revenue = st.number_input("Annual Revenue (RM)", min_value=50000, max_value=60000000, value=1000000)
existing_loan = st.selectbox("Existing Loan", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
credit_score = st.number_input("Credit Score", min_value=250, max_value=900, value=600)
num_employees = st.number_input("Number of Employees", min_value=1, max_value=600, value=10)
profit_margin = st.slider("Profit Margin (%)", min_value=3.0, max_value=35.0, value=10.0)
industry = st.selectbox("Industry", ['Manufacturing', 'Services', 'Agriculture', 'Construction', 'Retail'])
location = st.selectbox("Location", [
    'Johor', 'Kedah', 'Kelantan', 'Malacca', 'Negeri Sembilan', 
    'Pahang', 'Penang', 'Perak', 'Perlis', 'Sabah', 
    'Sarawak', 'Selangor', 'Terengganu', 'Kuala Lumpur'
])
sme_category = st.selectbox("SME Category", ['Micro', 'Small', 'Medium', 'Large'])

# Encode categorical inputs with fallback for unseen labels
if industry in label_encoder_industry.classes_:
    industry_encoded = label_encoder_industry.transform([industry])[0]
else:
    st.error(f"Unknown industry label: {industry}")
    industry_encoded = -1  # Default value for unknown labels

if location in label_encoder_location.classes_:
    location_encoded = label_encoder_location.transform([location])[0]
else:
    st.error(f"Unknown location label: {location}")
    location_encoded = -1  # Default value for unknown labels

if sme_category in label_encoder_category.classes_:
    sme_category_encoded = label_encoder_category.transform([sme_category])[0]
else:
    st.error(f"Unknown SME category label: {sme_category}")
    sme_category_encoded = -1  # Default value for unknown labels

# Create a DataFrame for the input
input_data = pd.DataFrame({
    "Business Age (years)": [business_age],
    "Annual Revenue (RM)": [annual_revenue],
    "Existing Loan": [existing_loan],
    "Credit Score": [credit_score],
    "Number of Employees": [num_employees],
    "Profit Margin (%)": [profit_margin],
    "Industry": [industry_encoded],
    "Location": [location_encoded],
    "SME Category": [sme_category_encoded]
})

# Predict loan eligibility
if st.button("Predict Loan Eligibility"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Eligible Loan Amount: RM {prediction:,.2f}")
    
    # Display results based on prediction with a less strict threshold
    eligibility_threshold = 5000  # Allow eligibility for predictions above RM5,000
    if prediction >= eligibility_threshold:
        st.success(f"The business is eligible for the loan.")
    else:
        st.warning(f"The business may not be eligible for the loan.")