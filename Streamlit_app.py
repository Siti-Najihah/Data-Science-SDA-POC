import streamlit as st


# Define pages using st.Page
Summary_page = st.Page(
    page="Projects/summary.py",
    title="Page Summary",
    icon="📝",
    default=True
)

Executive_summary_page = st.Page(
    page="Projects/explore_pagev2.py",
    title="Executive Summary",
    icon="📊",
)

Image_Classification_page = st.Page(
    page="Projects/Image_Classification.py",
    title="SDA Face Recognition",
    icon="🧑🏻",
)

Prediction_page = st.Page(
    page="Projects/predict_page.py",
    title="Salary Prediction",
    icon="⌛",
)

Loan_Default_page = st.Page(
    page=r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\Projects\loandefault.py",
    title="Loan Default Prediction",
    icon="💰"
)

Loan_MIA_page = st.Page(
    page="Projects/app.py",
    title="Loan MIA Prediction",
    icon="💰"
)

Phishing_page = st.Page(
    page="Projects/Phishing_Detection.py",
    title="Phishing Email Detection",
    icon="💻"
)

Loan_Eligibility_page = st.Page(
    page="Projects/loan_eligibility.py",
    title="Loan Eligibility Prediction",
    icon="🧾",
)

Loan_amt_predict_page = st.Page(
    page="Projects/loan_amt_predict.py",
    title="SME Loan Eligibility Amount Predictor",
    icon="🧾",
)

Procurement_Vendor_Selection_page = st.Page(
    page="Projects/app_rd.py",
    title="Procurement Vendor Selection System",
    icon="💻",
)

pg = st.navigation(
    {
        "Info": [Summary_page, Executive_summary_page],
        "Projects": [Loan_MIA_page, Loan_Default_page, Loan_Eligibility_page, Loan_amt_predict_page, Procurement_Vendor_Selection_page, Phishing_page, Prediction_page, Image_Classification_page],
    }
)

st.logo("Logo\CGC-Corporate-Logo-TL-Blue 2.png")
st.sidebar.text("Designed and developed by Data Science Team")

pg.run()







