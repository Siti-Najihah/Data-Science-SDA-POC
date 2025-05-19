import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st
data = pd.read_csv(r"c:\Users\sitinajihah.ms\OneDrive - cgcmb\Siti Najihah\New_Project_PE\spam.csv")

data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['ham', 'spam'],['Not Phishing', 'Phishing'])

mess = data['Message']
cat = data['Category']

(mess_train,mess_test,cat_train,cat_test) = train_test_split(mess, cat, test_size=0.2)

cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

#Creating Model

model = MultinomialNB()
model.fit(features, cat_train)

#Test our model
features_test = cv.transform(mess_test)
print(model.score(features_test, cat_test))

#Predict Data
def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result

st.header('Phishing Email Detection')

input_mess = st.text_input('Enter Message Here')
    
def predict_with_probability(message):
    input_message = cv.transform([message])
    probabilities = model.predict_proba(input_message)[0]  # [0] gets the first (and only) prediction
    phishing_index = list(model.classes_).index("Phishing")
    phishing_prob = probabilities[phishing_index]
    return phishing_prob

if st.button('Validate'):
    with st.spinner('Validating message...'):
        phishing_prob = predict_with_probability(input_mess)
        percent = phishing_prob * 100

        # Determine risk level, outcome message, and text color
        if percent >= 60:
            risk_level = "High likelihood of phishing attempt."
            outcome = f"This message exhibits characteristics consistent with phishing ({percent:.2f}% probability)."
            color = "red"
        elif percent >= 50:
            risk_level = "Moderate likelihood of phishing attempt. Verification by the security team is recommended."
            outcome = f"This message may contain indicators of phishing ({percent:.2f}% probability)."
            color = "orange"
        else:
            risk_level = "Low likelihood of phishing attempt."
            outcome = f"This message is unlikely to be a phishing attempt ({percent:.2f}% probability)."
            color = "green"

        # Display result with only the message text colored
        st.markdown(f'<p style="font-size:18px; color:{color};"><strong>Validation Outcome:</strong> {outcome}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:18px; color:{color};"><strong>Risk Category:</strong> {risk_level}</p>', unsafe_allow_html=True)
