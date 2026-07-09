import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="HR Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide"
)

st.sidebar.title("📌 Navigation")

st.sidebar.info(
    """
    **Project:** HR Employee Attrition Prediction

    **Algorithm:** Logistic Regression ML

    **Deployment:** Streamlit

    **Developer:** Ansh Ravat
    """
)


st.title("👨‍💼 HR Employee Attrition Prediction System")
with st.expander("ℹ️ About this Project"):

    st.write("""
    This application predicts whether an employee is likely to leave the company
    based on HR-related information.

    Model Used:
    - Logistic Regression
    - OneHotEncoder
    - Streamlit Deployment
    """)

st.markdown(
    """
    Enter the employee details below to predict whether the employee
    is likely to leave the company.
    """
)
st.divider()

model = joblib.load("model.joblib")
st.sidebar.success("✅ Model Loaded")

st.sidebar.write("Algorithm")
st.sidebar.code("Logistic Regression")
# st.success("Model Loaded Successfully ✅")

st.sidebar.write("Dataset")

st.sidebar.code(
"""
IBM HR Analytics
1470 Records
25 Features
"""
)

# df = pd.read_csv("HR-Employee-Attrition.csv")
# st.write(df.head())

st.subheader("👤 Personal Information")
# ==========================
# 👤 Personal Information
# ==========================


col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Employee Age", 18, 60, 30)

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    education = st.selectbox(
        "Education Level",
        [
            "1 - Below College",
            "2 - College",
            "3 - Bachelor",
            "4 - Master",
            "5 - Doctor"
        ]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        1,
        50,
        10
    )

st.divider()

# ==========================
# 💼 Job Information
# ==========================

st.subheader("💼 Job Information")

col1, col2 = st.columns(2)

with col1:

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    business_travel = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    daily_rate = st.number_input(
        "Daily Rate",
        100,
        2000,
        800
    )

    monthly_income = st.number_input(
        "Monthly Income",
        1000,
        200000,
        50000
    )

    num_companies_worked = st.number_input(
        "Companies Worked",
        0,
        20,
        2
    )

    overtime = st.selectbox(
        "OverTime",
        ["Yes", "No"]
    )

with col2:

    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        10,
        100,
        50
    )

    monthly_rate = st.number_input(
        "Monthly Rate",
        1000,
        30000,
        15000
    )

    percent_salary_hike = st.number_input(
        "Salary Hike (%)",
        0,
        30,
        15
    )

    years_at_company = st.number_input(
        "Years At Company",
        0,
        40,
        5
    )

    years_since_last_promotion = st.number_input(
        "Years Since Last Promotion",
        0,
        20,
        1
    )

st.divider()

# ==========================
# 😊 Satisfaction & Work Environment
# ==========================

st.subheader("😊 Satisfaction & Work Environment")

col1, col2 = st.columns(2)

rating = [
    "1 - Low",
    "2 - Medium",
    "3 - High",
    "4 - Very High"
]

with col1:

    environment_satisfaction = st.selectbox(
        "Environment Satisfaction",
        rating
    )

    job_involvement = st.selectbox(
        "Job Involvement",
        rating
    )

    work_life_balance = st.selectbox(
        "Work Life Balance",
        rating
    )

    training_times_last_year = st.selectbox(
        "Training Times Last Year",
        list(range(7))
    )

with col2:

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        rating
    )

    relationship_satisfaction = st.selectbox(
        "Relationship Satisfaction",
        rating
    )

    stock_option_level = st.selectbox(
        "Stock Option Level",
        [0, 1, 2, 3]
    )


# predict_button = st.button("Predict Attrition")
predict_button = st.button(
    "🔍 Predict Attrition",
    use_container_width=True
)

if predict_button:

# Convert dropdown text to numbers

    education = int(education[0])
    environment_satisfaction = int(environment_satisfaction[0])
    job_involvement = int(job_involvement[0])
    job_satisfaction = int(job_satisfaction[0])
    relationship_satisfaction = int(relationship_satisfaction[0])
    work_life_balance = int(work_life_balance[0])
    
    
    # Create dictionary
    input_data = {
        "Age": age,
        "BusinessTravel": business_travel,
        "DailyRate": daily_rate,
        "Department": department,
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EducationField": education_field,
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobRole": job_role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "OverTime": overtime,
        "PercentSalaryHike": percent_salary_hike,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option_level,
        "TrainingTimesLastYear": training_times_last_year,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsSinceLastPromotion": years_since_last_promotion,
    }

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame([input_data])


    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    stay_probability = probability[0] * 100
    leave_probability = probability[1] * 100

    st.divider()

    st.subheader("📊 Prediction Result")

    if prediction == 1:

        st.error("🔴 Employee is likely to Leave the Company.")

        st.metric(
            "Probability of Leaving",
            f"{leave_probability:.2f}%"
        )

        st.progress(int(leave_probability))

    else:

        st.success("🟢 Employee is likely to Stay in the Company.")

        st.metric(
            "Probability of Staying",
            f"{stay_probability:.2f}%"
        )
        st.progress(int(stay_probability))

st.divider()

st.caption(
    "Built using Streamlit • Scikit-Learn • Pandas"
)
