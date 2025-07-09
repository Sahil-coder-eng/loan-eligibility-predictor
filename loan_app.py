import streamlit as st
import pickle
import time

# Load the trained model
model = pickle.load(open('loan_model.pkl', 'rb'))

# App Title with Emoji and Center Alignment
st.markdown("<h1 style='text-align: center;'>🏦 Loan Eligibility Predictor</h1>", unsafe_allow_html=True)

# Personal Information Section
st.markdown("### 👤 Personal Information")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["No", "Yes"])
    dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])

with col2:
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Financial Info Section
st.markdown("### 💰 Financial Information")
col3, col4 = st.columns(2)

with col3:
    applicant_income = st.slider("Applicant Income", 0, 10000, 4000)
    loan_amount = st.slider("Loan Amount (in thousands)", 0, 700, 200)

with col4:
    coapplicant_income = st.slider("Coapplicant Income", 0, 5000, 1500)
    loan_term = st.selectbox("Loan Term (in days)", [360, 120, 240, 180])
    credit_history = st.selectbox("Credit History", [1.0, 0.0])

# Prediction Button
if st.button("🔍 Check Loan Eligibility"):
    # Format input data to match model features
    input_data = [
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        int(dependents.replace("3+", "3")),
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        2 if property_area == "Urban" else 1 if property_area == "Semiurban" else 0
    ]

    with st.spinner("⏳ Predicting... Please wait"):
        time.sleep(1.5)
        prediction = model.predict([input_data])[0]

    if prediction == 1:
        st.success("✅ Congratulations! Loan Approved.")
        st.balloons()
    else:
        st.error("❌ Sorry! Loan Not Approved.")
        st.snow()
