from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import shap

app = FastAPI(title="Credit Risk Decision API")


artifacts = joblib.load("model/credit_risk_model.pkl")

model = artifacts["model"]
t1 = artifacts["t1"]
t2 = artifacts["t2"]
features = artifacts["features"]

explainer = shap.TreeExplainer(model)




pay_cols = ["PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6"]

bill_cols = ["BILL_AMT1","BILL_AMT2","BILL_AMT3",
             "BILL_AMT4","BILL_AMT5","BILL_AMT6"]

amt_cols = ["PAY_AMT1","PAY_AMT2","PAY_AMT3",
            "PAY_AMT4","PAY_AMT5","PAY_AMT6"]





def feature_engineering(df):
    df = df.copy()

    df["late_months_count"] = (df[pay_cols] > 0).sum(axis=1)
    df["max_delay"] = df[pay_cols].max(axis=1)

    df["bill_mean_6m"] = df[bill_cols].mean(axis=1)
    df["pay_mean_6m"]  = df[amt_cols].mean(axis=1)

    df["util_mean_6m"] = df["bill_mean_6m"] / (df["LIMIT_BAL"] + 1)
    df["pay_to_bill_mean_6m"] = df["pay_mean_6m"] / (df["bill_mean_6m"] + 1)

    return df




class Applicant(BaseModel):
    data: dict



def credit_decision(p):

    if p < t1:
        return "APPROVE"

    elif p >= t2:
        return "REJECT"

    else:
        return "REVIEW"



@app.get("/")
def home():
    return {"message": "Credit Risk API Running"}

@app.get("/ping")
def ping():
  return {"status": "alive"}

@app.post("/predict")
def predict(applicant: Applicant):

    df = pd.DataFrame([applicant.data])

    
    df = feature_engineering(df)

    df = df[features]

    prob_default = model.predict_proba(df)[0][1]

    decision = credit_decision(prob_default)

    return {
        "default_probability": round(float(prob_default), 3),
        "decision": decision
    }



