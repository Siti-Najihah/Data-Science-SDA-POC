import streamlit as st

st.title("Page Summary")

st.write("\n")
st.subheader("Executive Summary", anchor=False)
st.write(
    """
    - The dashboard shows the summary of Power BI developer salary from 10 different countries
    - The data is represented in the Pie Chart and Bar Graph
    """
)

st.write("\n")
st.subheader("Machine Learning", anchor=False)
st.write(
    """
    1. Supervised Learning
        - Classification
        - Regression
    """
)

st.write(
    """
    2. Unsupervised Learning
        - Clustering 
    """
)

st.write("\n")
st.subheader("Projects", anchor=False)
st.write(
    """
    **Six** machine learning models have been developed, including **supervised classification** and **supervised regression models**
    """
)

st.write("\n")
st.subheader("1. Supervised Classification Model - SDA Face Recognition", anchor=False)
st.write(
    """
    The primary goal of this project is to develop a robust, easy-to-use face recognition system capable of identifying individuals from a small, predefined set of categories. This system is intended to be used in various scenarios, such as security systems, personalized access control, and automated identity verification processes. The model's ability to classify images in real-time allows for immediate feedback and efficient user interaction.
    \nThe project employs the following technologies:

1. **TensorFlow and Keras**: For developing and deploying the deep learning model.
2. **Streamlit**: For building an interactive web application that allows users to upload images and receive instant predictions.
3. **Python Libraries**: Including **NumPy, PIL** and **TensorFlow** utilities for image processing and model deployment.
    """
)

st.write("\n")
st.subheader("2. Supervised Classification Model - Phishing Email Detection", anchor=False)
st.write(
    """
    The main goal of this project is to develop a robust and efficient solution for detecting phishing emails from a large dataset of text-based messages. Phishing emails, which are often used for fraudulent activities like stealing personal information or spreading malware, are a common threat. This system is intended to automate the detection process, enabling users to quickly and accurately identify phishing attempts with minimal human intervention.
    \nThe project employs several technologies and tools to build and deploy the model:

1. **Python Libraries**:
    - **Pandas**: For data manipulation and handling the dataset.
    - **NumPy**: For numerical operations.
    - **Scikit-Learn**: For machine learning, including model training, feature extraction (**CountVectorizer**), and classification (**Multinomial Naive Bayes**).
2. **Streamlit**: For building an intuitive web interface, allowing users to interact with the model and receive predictions in real-time.
3. **CountVectorizer**: Used for converting text data (email messages) into numerical features suitable for the machine learning model.
    
**Application to CGC**: Email security for internal and external Communications
\n**Purpose**: Protect employees from phishing attacks in emails, especially since CGC likely deals with sensitive financial and personal information.
\n**How**: How: The model can be used to automatically analyze incoming emails to CGC employees. Emails flagged as "Phishing" can be routed to a security team for further analysis or can trigger an automatic alert to warn the recipient. This could protects CGC employees from opening fraudulent emails that could lead to data breaches, financial loss, or malware installation.
    """
)

st.write("\n")
st.subheader("3. Supervised Regression Model - Salary Prediction Tool", anchor=False)
st.write(
    """
    - This tool can be utilized to assist user to gauge the salary of a Power BI developer from different country
    - User needs to specify the country, qualification and years of working experience
    - The accuracy of this prediction tool is roughly 95%
    """
)
st.write(
    """
    The project employs several technologies to build and deploy the model:\n
    1. **Streamlit**: Utilized to build an interactive web app that allows users to input their details and get salary predictions in real time.
    2. **Pickle**: Used to load a pre-trained machine learning model (regressor), as well as the label encoders (le_country and le_education) that map categorical variables (country and education level) into numerical values required by the model.
    3. **NumPy**: Used for array manipulation and ensuring that the input data is in the right format (array) for the model to process.
    4. **Machine Learning Model (Regressor)**: The regressor model is a machine learning model that has been trained on historical salary data and is used to predict the annual salary based on user inputs.
    """
)
st.write(
    """
\n**Application to CGC**: Salary benchmarking for Power BI developers
\n**Purpose**: With CGC being a major financial institution, it is essential to have competitive and accurate salary offerings for tech roles. The model can be used to benchmark the salary expectations for Power BI developers based on factors like **experience**, **state**, and **education level**.
\n**How**: HR departments could use this tool to estimate appropriate salary ranges when hiring or negotiating salaries for developers, ensuring CGC stays competitive in the job market.        
    """
)





st.write("\n")
st.subheader("4. Supervised Classification Model - Loan MIA Prediction", anchor=False)
st.write(
    """
    The goal of this ML model is to predict whether a loan customer will become **Month-In-Arrears (MIA)** in the next 3 months. The goal is to help the Guarantee Monitoring & Reporting (GMR) Department proactively monitor and manage loan defaults.

\n **Objective**: Predict if a customer will be MIA (i.e., miss payments) in the next 3 months based on historical loan and customer data.\n
**Data**: The model uses features such as loan amount, guarantee cover amount, outstanding balance, interest rate, race, bumi status, constitution, sector, scheme group, and financial entity.\n
**Label**: The target variable is created by checking if a customer (grouped by appl_no) has a MIA event in the next 3 months.\n
**Algorithm**: The model uses a **RandomForestClassifier** from scikit-learn, which is an ensemble learning method based on decision trees.\n
**Usage**: This predictive model can be used by the Guarantee Monitoring & Reporting (GMR) Department to identify high-risk loans and take early action to reduce defaults.
    """
)

st.write("\n")
st.subheader("5. Supervised Regression Model - Loan Eligibility Prediction", anchor=False)
st.write(
    """
    - A Loan Eligibility Prediction model using a **Random Forest Classifier** was developed to automate and enhance the loan approval process.
    - The model uses key features like **income, credit score, and loan amount** to predict eligibility and trained on a **synthetic dataset of 50,000 samples**
    - The benefit of this model is **reduces human bias, improves decision speed**, and **minimizes loan default risks**, making the approval process more efficient and reliable.
    - The impact of this model is supports multiple departments i.e. **Credit Risk, Loan Processing, Customer Service, Marketing, and Finance**—with faster, data-driven insights and improved workflow.
    """
)
st.write(
    """
The project employs several technologies to build and deploy the model:\n
1. **Streamlit**: Utilized to create a web interface for easy user interaction, allowing them to input business details and receive loan eligibility predictions.
2. **Joblib**: Used to load pre-trained machine learning models (loan_eligibility_model.pkl) and the corresponding feature list (model_features.pkl) for prediction.
3. **Pandas**: Used to organize and structure the user inputs into a DataFrame format compatible with the model's expected input.
4. **Machine Learning Model**: A classifier model trained to predict loan eligibility based on business attributes such as credit score, annual revenue, and industry. 
    """
)
st.write(
    """
**Application to CGC**: Loan approval process
\n**Purpose**: To automate and optimize the loan approval process by predicts loan eligibility based on key applicant data (e.g., income, credit score, and loan amount), thereby reducing human bias, increasing decision-making speed, and minimizing the risk of loan defaults.
\n**How**: Credit Risk, Loan Processing, Customer Service, Marketing, and Finance departments can leverage this model to gain faster, data-driven insights and streamline decision-making processes.
    """
)

st.write("\n")
st.subheader("6. Supervised Regression Model - SME Loan Eligibility Amount Predictor", anchor=False)
st.write(
    """
    - Developed a machine learning model (SME Loan Eligibility Amount Predictor) to estimate eligible loan amounts based on business-specific attributes like company size, business age, and employee count.
    - Utilized a Random Forest Regressor trained on a 50,000-sample dummy dataset generated by CoPilot.
    - Designed to support Branch Sales Management, Credit Risk, and Product Development teams in financial institutions.
    - Aims to streamline SME loan evaluations, enhance credit decision-making, and improve customer accessibility.
    """
)
st.write(
    """
    The project employs several technologies to build and deploy the model:\n
    1. **Streamlit**: Utilized for creating an interactive web interface for users to input data and view the results.
    2. **Joblib**: Used to load the pre-trained machine learning model (sme_loan_model.pkl) and the LabelEncoder objects for encoding categorical features.
    3. **Pandas**: Used to manage and structure input data into a format compatible with the model.
    4. **Scikit-learn**: Utilized for encoding categorical features (LabelEncoder) and for prediction tasks with the pre-trained model.
    """
)
st.write(
    """
**Application to CGC**: Loan eligibility prediction for SMEs
\n**Purpose**: To streamline SME loan evaluations and improve credit decision-making by estimating eligible loan amounts using a Random Forest Regressor trained on business-specific attributes such as company size, business age, and employee count.
\n**How**: Branch Sales Management, Credit Risk, and Product Development teams can leverage this model to enhance loan assessments, develop tailored financial products, and improve customer accessibility.
    """
)

st.write("\n")
st.subheader("7. Supervised Regression Model - Procurement Vendor Selection System", anchor=False)
st.write(
    """
This machine learning prototype leverages a neural network model to automate and optimize the supplier selection process using historical data such as cost, quality score, delivery time, and reliability. 
 
1. The pipeline includes data preprocessing, training with early stopping to prevent overfitting, and explainability using SHAP for feature importance. 
2. The model achieved strong accuracy and is saved for deployment, making it scalable and reusable. 
3. This solution benefits procurement managers, supply chain teams, and decision-makers by improving the consistency, speed, and fairness of supplier evaluation. 
4. Its implementation can lead to more strategic supplier choices, reduced operational risks, and enhanced cost-efficiency for the company.
    """
)
