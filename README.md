# Credit Risk Scoring System

An end-to-end machine learning system that predicts customer default risk and translates it into real-world lending decisions with explainability.



## Overview

- Built a complete **credit risk pipeline** using LightGBM  
- Converts model outputs into **APPROVE / REVIEW / REJECT** decisions  
- Designed to reflect **real-world banking workflows**  
- Integrated **SHAP explainability** for transparent predictions  



## Objectives

- Predict probability of customer default  
- Design a **threshold-based decision system**  
- Ensure consistency between training and inference  
- Provide **interpretable outputs** using SHAP  
- Build a deployable ML system (not just a model)



## Model Details

- **Algorithm:** LightGBM Classifier  
- **Type:** Binary classification (default probability)  
- **Decision Layer:** Multi-class (Approve / Review / Reject)  
- **Metric Used:** PR-AUC (handles imbalanced data effectively)  



## Feature Engineering

- Late payment behavior (`late_months_count`)  
- Maximum delay (`max_delay`)  
- Average bill amount (`bill_mean_6m`)  
- Average payment amount (`pay_mean_6m`)  
- Credit utilization trends (`util_mean_6m`)  
- Payment-to-bill ratio (`pay_to_bill_mean_6m`)  



## System Architecture

- **Streamlit:** Collects user inputs interactively  
- **FastAPI:** Handles requests and model inference  
- **Feature Engineering:** Ensures training–inference consistency  
- **Model:** Predicts default probability  
- **Decision Engine:** Converts probability → business decision  
- **SHAP:** Explains *why* the decision was made



## Explainability (SHAP)

- Identifies **top risk-driving features**  
- Highlights factors contributing to **approval or rejection**  
- Provides **transparent decision reasoning**  



## Key Highlights

- End-to-end ML system (Model + API + UI)  
- Real-world **decision-based approach** instead of raw predictions  
- Strong focus on **interpretability and deployment**  
- Clean modular structure suitable for production systems  



## Conclusion

- Demonstrates how ML models are used in **financial decision systems**  
- Bridges the gap between **prediction and business logic**  
- Showcases skills in **ML, backend development, and system design**  
