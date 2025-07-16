import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('rf_model.pkl', 'rb'))

st.title("💼 IBM HR Attrition Predictor")
st.write("Fill the employee details to predict whether they are likely to leave.")

# --- USER INPUT FIELDS ---
age = st.slider("Age", 18, 60, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
monthly_income = st.number_input("Monthly Income", 1000, 200000, 50000)
total_working_years = st.slider("Total Working Years", 0, 40, 10)
years_at_company = st.slider("Years at Company", 0, 30, 5)
job_role = st.selectbox("Job Role", [
    'Sales Executive', 'Research Scientist', 'Laboratory Technician',
    'Manufacturing Director', 'Healthcare Representative', 'Manager',
    'Sales Representative', 'Research Director', 'Human Resources'
])
overtime = st.selectbox("OverTime", ['Yes', 'No'])
work_life_balance = st.selectbox("WorkLifeBalance (1-Bad to 4-Best)", [1, 2, 3, 4])
job_involvement = st.selectbox("JobInvolvement (1-Low to 4-Very High)", [1, 2, 3, 4])
job_satisfaction = st.selectbox("JobSatisfaction (1-Low to 4-Very High)", [1, 2, 3, 4])
env_satisfaction = st.selectbox("EnvironmentSatisfaction (1-Low to 4-Very High)", [1, 2, 3, 4])
performance_rating = st.selectbox("PerformanceRating (1-Low to 4-Outstanding)", [1, 2, 3, 4])

# --- ENCODE MANUAL INPUT ---
input_dict = {
    'Age': age,
    'MonthlyIncome': monthly_income,
    'TotalWorkingYears': total_working_years,
    'YearsAtCompany': years_at_company,
    'WorkLifeBalance': work_life_balance,
    'JobInvolvement': job_involvement,
    'JobSatisfaction': job_satisfaction,
    'EnvironmentSatisfaction': env_satisfaction,
    'PerformanceRating': performance_rating,
    'Gender_Male': 1 if gender == "Male" else 0,
    'OverTime_Yes': 1 if overtime == "Yes" else 0
}

# One-hot encode job role (all options must match training)
job_roles = [
    'Healthcare Representative', 'Human Resources', 'Laboratory Technician',
    'Manager', 'Manufacturing Director', 'Research Director',
    'Research Scientist', 'Sales Executive', 'Sales Representative'
]
for role in job_roles:
    input_dict[f'JobRole_{role}'] = 1 if job_role == role else 0

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Align columns with model
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model.feature_names_in_]

# --- PREDICT BUTTON ---
if st.button("Predict"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("📊 Prediction Result")
    if pred == 1:
        st.error(f"❌ The employee is likely to leave.\n\nProbability: {prob:.2%}")
    else:
        st.success(f"✅ The employee is likely to stay.\n\nProbability: {prob:.2%}")
