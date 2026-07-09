import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Loan Rejection Predictor", page_icon="🏦")

st.title("🏦 Loan Rejection Risk Predictor")

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

st.write("Enter customer information below.")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)
inccat_dict = {
    1: "0-20 L",
    2: "20-39.9 L",
    3: "40-59.9 L",
    4: "60-79.9 L",
    5: "80-89.9 L",
    6: "90-99.99 L",
    7: "1-20 Cr"
}
income = st.selectbox(
    "Income Category",
    inccat_dict.keys(),
    format_func=lambda x: f"{x} - {inccat_dict[x]}"
)

rating = {
    1: "Very Low",
    2: "Low",
    3: "Moderate",
    4: "High",
    5: "Very High",
    6: "Extremely High"
}

#networth = st.selectbox(
    #"Net Worth Category",
    #rating
#)
networth = st.selectbox(
    "Net Worth Category",
    rating.keys(),
    format_func=lambda x: f"{x} - {rating[x]}"
)

#asset = st.selectbox(
    #"Asset Category",
    #rating
#)
asset = st.selectbox(
    "Asset Category",
    rating.keys(),
    format_func=lambda x: f"{x} - {rating[x]}"
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "AGE":[age],
        "INCCAT":[income],
        "NWCAT":[networth],
        "ASSETCAT":[asset]
    })

    input_scaled = scaler.transform(input_df)

    cluster = model.predict(input_scaled)[0]

    st.divider()
    st.info(
        """
        **Note:**

        This prediction is based on customer segmentation using
        the K-Means Clustering algorithm.

        It estimates the customer's loan rejection risk level and
        should not be considered an actual bank decision.
        """
    )

    if cluster == 0:

        st.success("🟢 Low Loan Rejection Risk")

    elif cluster == 1:

        st.error("🔴 High Loan Rejection Risk")

    else:

        st.warning("🟡 Medium Loan Rejection Risk")

st.divider()

st.caption(
    "Built by ANSH using Python • Streamlit • Scikit-Learn • K-Means Clustering"
)