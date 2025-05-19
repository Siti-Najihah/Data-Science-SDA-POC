import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle

# Load the trained model
model = tf.keras.models.load_model(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\harith\PRD Automated Supplier Selection\supplier_selection_model.h5")

# Load the preprocessor
with open(r"C:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\harith\PRD Automated Supplier Selection\preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

# Check if the preprocessor is fitted
if not hasattr(preprocessor, 'transform'):
    st.error("The preprocessor is not fitted. Please ensure it is correctly loaded and fitted.")

# Streamlit app title
st.markdown("<h1 style='text-align: center;'>Procurement Vendor Selection System</h1>", unsafe_allow_html=True)

# Layout: Input form in an expander
with st.expander("Enter Vendor Details", expanded=True):
    st.markdown("#### Vendor Information ####")
    col1, col2 = st.columns(2)

    with col1:
        cost = st.number_input("Cost (MYR)", min_value=2000.0, max_value=50000.0, step=100.0)
        quality_score = st.slider("Quality Score (1-10)", min_value=1, max_value=10, step=1)
        delivery_time = st.number_input("Delivery Time (days)", min_value=1.0, max_value=60.0, step=1.0)
        reliability_score = st.slider("Reliability Score (1-10)", min_value=1, max_value=10, step=1)

    with col2:
        past_performance = st.number_input("Past Performance (%)", min_value=50.0, max_value=100.0, step=1.0)
        supplier_location = st.selectbox("Supplier Location", ["Local", "Regional", "International"])
        certifications = st.selectbox("Certifications", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        contract_length = st.number_input("Contract Length (months)", min_value=6, max_value=36, step=1)
        discount_offered = st.number_input("Discount Offered (%)", min_value=0.0, max_value=20.0, step=0.1)
        industry_sector = st.selectbox("Industry Sector", ["Manufacturing", "IT", "Logistics"])

# Reliability Score Interpretation
st.markdown("### Reliability Assessment")
if reliability_score >= 9:
    reliability_category = "Very reliable – top-tier supplier"
elif 7.5 <= reliability_score < 9:
    reliability_category = "Generally reliable – low risk"
elif 6 <= reliability_score < 7.5:
    reliability_category = "Moderate reliability – monitor closely"
else:
    reliability_category = "Unreliable – high risk supplier"

st.info(f"**Assessment Result:** {reliability_category}")

# Predict button
if st.button("Predict"):
    # Create a DataFrame for the input
    input_data = pd.DataFrame([{
        "Cost": cost,
        "Quality_Score": quality_score,
        "Delivery_Time": delivery_time,
        "Reliability_Score": reliability_score,
        "Past_Performance": past_performance,
        "Supplier_Location": supplier_location,
        "Certifications": certifications,
        "Contract_Length": contract_length,
        "Discount_Offered": discount_offered,
        "Industry_Sector": industry_sector
    }])

    if hasattr(preprocessor, 'transform'):
        try:
            # Preprocess the input data
            processed_data = preprocessor.transform(input_data)

            # Make prediction
            prediction_probabilities = model.predict(processed_data)
            selected_probability = prediction_probabilities[0][0] * 100
            not_selected_probability = 100 - selected_probability

            result = "Selected" if selected_probability > 50 else "Not Selected"

            # Display the result
            st.markdown("### Assessment Result")

            # Conditional display with styled output
            if result == "Selected":
                st.markdown(
                    f"""
                    <div style="padding: 1rem; border-radius: 10px; background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb;">
                        <strong>The vendor is {result}.</strong><br>
                        Vendor Result: <strong>{selected_probability:.2f}%</strong> for Selected, <strong>{not_selected_probability:.2f}%</strong> for Not Selected
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="padding: 1rem; border-radius: 10px; background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;">
                        <strong>The vendor is {result}.</strong><br>
                        Vendor Result: <strong>{selected_probability:.2f}%</strong> for Selected, <strong>{not_selected_probability:.2f}%</strong> for Not Selected
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        except Exception as e:
            st.error(f"Error during transformation or prediction: {e}")
    else:
        st.error("Preprocessor is not fitted. Please ensure it is correctly loaded and fitted.")
