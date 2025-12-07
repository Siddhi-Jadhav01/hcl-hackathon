# hcl-hackathon
AI Python based HCL Hackathon.
📌 1. Project Overview

This project predicts whether a customer will return an item (Yes/No) based on historical transaction data.
Returns have a major impact on revenue, logistics, and customer experience.
Using machine learning, we classify each purchase as Returned (1) or Not Returned (0).

🎯 2. Objective

Build a classification model that predicts if an order will be returned.

Use retail transactional data containing customer, product, revenue, refund, and order details.

Deploy a simple UI interface for real-time predictions.

🧹 3. Data Cleaning

Steps followed:

✔ Handle missing values
✔ Convert date features into usable numerical form
✔ Normalize column formats (numeric, categorical)
✔ Remove duplicates
✔ Fix inconsistent categories
✔ Drop irrelevant or high-cardinality columns

🔍 4. Feature Selection

To improve performance and reduce training complexity, only important predictive features were retained.

🧬 5. Feature Engineering

To strengthen signal and model interpretability

🔀 6. Train–Test Split

Dataset is split using stratified sampling:

Train: 80%
Test: 20%

🤖 7. Modeling – Ensemble Approach

To achieve the best classification performance, an Ensemble Stacked Model is used.
It combines:

Base Models

Logistic Regression

Random Forest Classifier

XGBoost Classifier

Meta Model

Logistic Regression (stacking layer)

📈 8. Model Evaluation

Metrics evaluated:

Accuracy

Precision

Recall (most important for identifying returns)

F1-Score

ROC-AUC Score

Confusion Matrix
