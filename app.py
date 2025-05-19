# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load(r'C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\afif\LoanMIAprediction\rf_model.joblib')
model_columns = joblib.load(r'C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\Streamlit_Multipage_App\afif\LoanMIAprediction\model_columns.txt')

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="120"/>
        <h1>Loan MIA Prediction</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "This app predicts whether a customer will Month-In-Arrears (MIA) on their loan in the next 3 months based on the provided information."
)
st.info(
    "Please fill in all the fields below and click the **Predict** button to see the prediction result."
)

# Create two columns
col1, col2 = st.columns(2)

with col1:
    
    race_desc = st.selectbox('Race', ['MALAYS', 'CHINESE', 'INDIAN', 'OTHERS'])
    bumi_status = st.selectbox('Bumi Status', ['BUMI', 'NON-BUMI'])
    constitution = st.selectbox('Constitution', [
        'SDN BHD/ PRIVATE LTD', 'PARTNERSHIP', 'SOLE PROPRIETOR', 'LIMITED LIABILITY PARTNERSHIP (LLP)', 'PROFESSIONALS', 'INDIVIDUAL', 'BERHAD/COMPANY LIMITED BY SHARES'
    ])
    sector_desc = st.selectbox('Sector', [
        'MANUFACTURING', 'TRANSPORT, STORAGE & COMMUNICATION', 'WHOLESALE & RETAIL TRADE & RESTAURANTS & HOTELS', 'FINANCING, INSURANCE, REAL ESTATE & BUSINESS SERVICES', 'COMMUNITY, SOCIAL & PERSONAL SERVICES', 'CONSTRUCTION', 'AGRICULTURE, HUNTING, FORESTRY & FISHING', 'ELECTRICITY, GAS & WATER', 'MINING & QUARRYING'
    ])
    fi_entity = st.selectbox('FI Name', [
        'MODALKU VENTURES SDN BHD (FUNDING SOCIETIES)', 'ALLIANCE BANK MALAYSIA BERHAD', 'AMBANK ISLAMIC BERHAD', 'CIMB ISLAMIC BANK BERHAD', 'AMBANK (M) BERHAD', 'ALLIANCE ISLAMIC BANK BERHAD', 'OCBC BANK (MALAYSIA) BERHAD', 'BANK KERJASAMA RAKYAT MALAYSIA', 'RHB BANK BERHAD', 'RHB ISLAMIC BANK BERHAD', 'MALAYAN BANKING BERHAD', 'STANDARD CHARTERED BANK MALAYSIA BERHAD', 'STANDARD CHARTERED SAADIQ BERHAD', 'HSBC BANK MALAYSIA BERHAD', 'AFFIN ISLAMIC BANK BERHAD', 'OCBC AL-AMIN BANK BERHAD', 'HONG LEONG BANK BERHAD', 'PUBLIC BANK BERHAD', 'AFFIN BANK BERHAD', 'CIMB BANK BERHAD', 'AXIATA DIGITAL CAPITAL SDN BHD', 'BANK SIMPANAN NASIONAL', 'MAYBANK ISLAMIC BERHAD', 'BANK PERTANIAN MALAYSIA BERHAD', 'SMALL MEDIUM ENTERPRISE DEVELOPMENT BANK MALAYSIA BERHAD', 'UNITED OVERSEAS BANK (MALAYSIA) BHD', 'HONG LEONG ISLAMIC BANK', 'BANK MUAMALAT MALAYSIA BERHAD'
    ])

with col2:

    scheme_code = st.selectbox('Scheme Code', ['6B', '1B', '9V', '6Y', '2D', '5Y', '7Y', '1D', '9Q', '4R', '4N', 'C8', '8R', '6F', '1C', '3N', '7B', '1J', '8B', '6L', '1M', 'P3', '7J', '1N', '5J', '5N', '4K', '2P', '2K', 'W9', '3P', '6K', '7R', '2X', '6P', 'X7', '2N', '2J', '9J', '7F', '2M', '4J', '6N', '8D', '8W', '9W', '9E', '5D', '3M', 'L8', '7W', '6M', '7X', 'L9', 'X9', 'N9', '1F', '9R', '3F', '8E', '9D', '8K', '9K', '1K', '4D', '3K', '5K', '7K', '5V', '7P', '3V', '1V', '5C', '8C', '3C', '7V', '3X', '3U', '1X', '7C', '2F', '1R', '7M', '7Q', '2U', '4X', '6X', '5X', '9X', '1U', '6D', '7E', '8J', '4B', 'L7', 'X8', '8Q', 'L6', '6J', '9M', 'C7', '3B', '3J', 'C9', '6R', '8M', 'B7', '2R', 'P8', '4U', 'K7', 'K8', '5B', '4C', '7L', '2Y', '1E', '9P', '1P', '5P', '8P', '2V', '4V', '9C', '6V', '8V', '6C', '4P', 'P9', '2L', 'X2', '4W', '1W', '5W', '2W', '3W', '6W', '2E', '5A', 'H6', 'H7', '1A', '1L', 'E8', 'S6', 'D7', '5M', 'D8', '9N', '5L', '9U', 'C6', '8U', '8F', '8L', '4M', '9F', '2B', 'LE', 'W8', '7N', '4L', 'W7', '5U', '8N', 'B9', '3R', '3L', '9H'])
    loan_amt = st.number_input('Loan Amount', min_value=0.0)
    gtee_cover_amt = st.number_input('Guarantee Cover Amount', min_value=0.0)
    outstd_bal = st.number_input('Outstanding Balance', min_value=0.0)
    schemes_group = st.selectbox('Scheme Group', ['PG', 'WG', 'Full_Risk', 'OSR', 'SHARE'])

interest_rate = st.number_input('Interest Rate', min_value=0.0)
    
if st.button('Predict'):
    # Prepare input as DataFrame
    input_dict = {
        'scheme_code': scheme_code,
        'loan_amt': loan_amt,
        'gtee_cover_amt': gtee_cover_amt,
        'outstd_bal': outstd_bal,
        'schemes_group': schemes_group,
        'interest_rate': interest_rate,
        'race_desc': race_desc,
        'bumi_status': bumi_status,
        'constitution': constitution,
        'sector_desc': sector_desc,
        'fi_entity': fi_entity
    }
    input_df = pd.DataFrame([input_dict])

    # One-hot encode categorical columns to match training
    categorical_cols = ['race_desc', 'bumi_status', 'constitution', 'sector_desc', 'schemes_group', 'fi_entity']
    input_df = pd.get_dummies(input_df, columns=categorical_cols)
    # Align columns with training columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Predict
    pred = model.predict(input_df)[0]
    if pred == 1:
        st.error('Prediction: Customer will MIA in the next 3 months')
    else:
        st.success('Prediction: Customer will not MIA in the next 3 months')