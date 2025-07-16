🧠 IBM HR Analytics – Employee Attrition Prediction

This project analyzes and predicts employee attrition using IBM's fictional HR dataset. It includes data preprocessing, exploratory data analysis (EDA), machine learning models, and a deployed Streamlit web app for real-time predictions based on user input.


📊 Problem Statement

Human Resource (HR) departments want to know:
- Why do employees leave?
- Can we predict attrition and act early?

This project provides insights into attrition trends and builds a machine learning model to predict whether an employee is likely to leave the company.


📁 Project Structure

├── HR-Employee-Attrition.csv       # Dataset
├── HR_attrition_code.ipynb         # Jupyter Notebook (EDA + ML)
├── rf_model.pkl                    # Trained Random Forest model
├── app.py                          # Streamlit app for live predictions
├── images/                         # Screenshots of the app
│   ├── employee_stay.png
│   └── employee_leave.png
└── README.md                       # Project documentation


🚀 How to Run the App

🔧 Install requirements:
```bash
pip install pandas numpy scikit-learn streamlit matplotlib seaborn
```

▶️ Run the Streamlit app:
```bash
streamlit run app.py
```
You’ll see a form to input employee details and get an instant prediction with probability.


🧠 Machine Learning Models Used

- **Random Forest Classifier**
- **Logistic Regression** (for comparison)

Key Features Used:
- Age, Gender, Monthly Income, OverTime
- Job Role, WorkLifeBalance, Job Satisfaction
- Environment Satisfaction, Total Working Years
- Performance Rating, and more


📈 Key Insights from EDA
- High attrition among employees with:
  - OverTime = Yes
  - Low WorkLifeBalance & JobSatisfaction
  - Sales Representative & Lab Technician roles
- MonthlyIncome and TotalWorkingYears negatively correlated with attrition


🛠️ Tools & Technologies
- **Python**, **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn** (EDA)
- **Scikit-learn** (ML)
- **Streamlit** (Web App)


👩‍💻 Developed By

**Gauri Mangesh Fargade**  
📍 Computer Engineering Student, SPPU  
📧 fargadegauri@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/gauri-fargade)

---

## 🌟 If You Liked This Project
Don’t forget to ⭐ star the repo and follow for more!

