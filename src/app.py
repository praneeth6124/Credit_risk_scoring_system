import streamlit as st
import requests

st.title("💳 Credit Risk Predictor")

st.write("Enter applicant details:")

# -------- BASIC INFO --------

limit_bal = st.number_input("Credit Limit", value=200000)

sex = st.selectbox("Sex", [1,2], format_func=lambda x: "Male" if x==1 else "Female")

education = st.selectbox(
    "Education",
    [1,2,3,4],
    format_func=lambda x:
        ["Graduate","University","High School","Others"][x-1]
)

marriage = st.selectbox(
    "Marriage",
    [1,2,3],
    format_func=lambda x:
        ["Married","Single","Others"][x-1]
)

age = st.slider("Age", 21, 75, 30)

# -------- PAYMENT HISTORY --------

st.subheader("Payment History")

pay_0 = st.number_input("PAY_0", value=0)
pay_2 = st.number_input("PAY_2", value=0)
pay_3 = st.number_input("PAY_3", value=0)
pay_4 = st.number_input("PAY_4", value=0)
pay_5 = st.number_input("PAY_5", value=0)
pay_6 = st.number_input("PAY_6", value=0)

# -------- BILL --------

st.subheader("Bill Amount")

bill1 = st.number_input("BILL_AMT1", value=5000)
bill2 = st.number_input("BILL_AMT2", value=4000)
bill3 = st.number_input("BILL_AMT3", value=3000)
bill4 = st.number_input("BILL_AMT4", value=2000)
bill5 = st.number_input("BILL_AMT5", value=1000)
bill6 = st.number_input("BILL_AMT6", value=500)

# -------- PAYMENTS --------

st.subheader("Payment Amount")

pay_amt1 = st.number_input("PAY_AMT1", value=2000)
pay_amt2 = st.number_input("PAY_AMT2", value=2000)
pay_amt3 = st.number_input("PAY_AMT3", value=1500)
pay_amt4 = st.number_input("PAY_AMT4", value=1000)
pay_amt5 = st.number_input("PAY_AMT5", value=800)
pay_amt6 = st.number_input("PAY_AMT6", value=500)

# ---------- PREDICT BUTTON ----------

if st.button("Predict Risk"):

    payload = {
        "data": {
            "LIMIT_BAL": limit_bal,
            "SEX": sex,
            "EDUCATION": education,
            "MARRIAGE": marriage,
            "AGE": age,

            "PAY_0": pay_0,
            "PAY_2": pay_2,
            "PAY_3": pay_3,
            "PAY_4": pay_4,
            "PAY_5": pay_5,
            "PAY_6": pay_6,

            "BILL_AMT1": bill1,
            "BILL_AMT2": bill2,
            "BILL_AMT3": bill3,
            "BILL_AMT4": bill4,
            "BILL_AMT5": bill5,
            "BILL_AMT6": bill6,

            "PAY_AMT1": pay_amt1,
            "PAY_AMT2": pay_amt2,
            "PAY_AMT3": pay_amt3,
            "PAY_AMT4": pay_amt4,
            "PAY_AMT5": pay_amt5,
            "PAY_AMT6": pay_amt6
        }
    }

    response = requests.post(
        "https://credit-risk-scoring-system-5k5d.onrender.com/predict",
        json=payload
    )

    if response.status_code == 200:

        result = response.json()

        decision = result["decision"]

        if decision == "APPROVE":
            st.success("✅ Loan Approved")

        elif decision == "REJECT":
            st.error("❌ Loan Rejected")

        else:
            st.warning("⚠️ Needs Manual Review")

    else:
        st.error("API Error")




