# 🛍️ AI-Powered Customer Return Prediction System

> Predict high-risk product returns before they happen using Machine Learning and Ensemble Learning.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## Overview

Product returns are a major challenge for e-commerce companies, leading to:

* Increased logistics costs
* Refund processing expenses
* Inventory management issues
* Reduced operational efficiency

This project uses Machine Learning to predict the probability of a customer returning a purchased product based on customer behavior, product characteristics, pricing information, and transaction history.

The system enables retailers to proactively identify high-risk orders and take preventive actions such as targeted customer support, product recommendations, or fraud investigation.

---
## Live Application

[https://hcl-hackathon-retailreturnclassification.streamlit.app/](https://hcl-hackathon-retailreturnclassification.streamlit.app/)

## Key Features

✅ End-to-End Machine Learning Pipeline

✅ Ensemble Stacking Architecture

✅ Advanced Feature Engineering

✅ Probability-Based Risk Scoring

✅ Interactive Streamlit Web Application

✅ Production-Ready Model Serialization

✅ Real-Time Predictions

---

## Business Problem

Returns cost online retailers billions of dollars annually.

Most companies react after a return occurs.

This system shifts the process from:

**Reactive Returns Management → Predictive Returns Prevention**

By identifying return-prone purchases beforehand, businesses can:

* Reduce return-related losses
* Improve customer satisfaction
* Optimize logistics operations
* Improve inventory planning

---

## Solution Architecture

```text
User Input
     │
     ▼
Streamlit Web App
     │
     ▼
Feature Engineering Layer
     │
     ▼
Stacked Ensemble Model
     │
     ▼
Return Probability Prediction
     │
     ▼
Business Decision Support
```

---

## Dataset Features

### Customer Features

* Age
* Gender
* Income Bracket
* Loyalty Program
* Membership Duration
* Customer Support Calls
* Days Since Last Purchase

### Product Features

* Category
* Subcategory
* Brand
* Price
* Discount
* Product Rating
* Review Count
* Historical Product Return Rate

### Transaction Features

* Quantity
* Total Items Purchased
* Season
* Weekend Indicator
* Holiday Season Indicator

---

## Data Preprocessing

### Missing Value Handling

* Numerical Features → Median Imputation
* Categorical Features → Most Frequent / Unknown

### Feature Encoding

* One-Hot Encoding
* Boolean Standardization

### Data Cleaning

* Duplicate Removal
* Category Standardization
* Outlier Validation

### Feature Scaling

* Numerical Feature Normalization

---

## Feature Engineering

Several domain-specific features were created to improve predictive performance:

### Pricing Features

```python
final_price = price - discount
discount_ratio = discount / price
```

### Customer Features

```python
is_loyal = 1 if loyalty_program == "Yes"
```

### Purchase Features

```python
value_per_item = final_price / quantity
```

These engineered features improved the model's ability to capture purchasing patterns associated with returns.

---

## Machine Learning Models

### Base Models

#### Logistic Regression

* Captures global linear relationships
* Interpretable baseline model

#### Random Forest

* Handles non-linear interactions
* Robust against overfitting

#### XGBoost

* Captures complex decision boundaries
* Strong performance on tabular datasets

---

## Stacking Ensemble

The final prediction is generated using a Stacking Ensemble Architecture.

```text
               Logistic Regression
                        │
                        ▼
               Random Forest
                        │
                        ▼
                    XGBoost
                        │
                        ▼
             Meta Logistic Regression
                        │
                        ▼
                 Final Prediction
```

The meta-model learns the optimal combination of predictions from all base learners, resulting in better performance than individual models.

---

## Model Evaluation

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

### Why Recall Matters

In return prediction systems, missing an actual return is often more costly than a false alarm.

Therefore, Recall was treated as a primary optimization metric.

---

## Streamlit Application

The application provides a simple interface where users can enter:

* Customer Age
* Product Price
* Discount
* Product Return Rate
* Quantity
* Loyalty Program Status

The system then predicts:

### Output

```text
Prediction: Returned / Not Returned

Return Probability: 84%
```

### Risk Classification

* ⚠️ High Return Risk
* ✅ Low Return Risk

---

## Tech Stack

### Programming

* Python

### Machine Learning

* Scikit-Learn
* XGBoost

### Data Processing

* Pandas
* NumPy

### Deployment

* Streamlit

### Model Persistence

* Joblib

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-return-prediction.git

cd customer-return-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

## Future Improvements

### Explainable AI

* SHAP Value Analysis
* Feature Importance Dashboard

### MLOps

* Docker Containerization
* CI/CD Pipeline
* Automated Retraining

### Deployment

* FastAPI Backend
* AWS/GCP Deployment
* Real-Time Prediction API

### Monitoring

* Data Drift Detection
* Model Performance Tracking
* Prediction Monitoring Dashboard

---

## Hackathon Project

Developed as part of an ML Hackathon challenge focused on solving real-world retail analytics problems using machine learning and predictive modeling.

---

## Author

**Siddhi Jadhav**

Aspiring Data Scientist | Machine Learning Engineer

* LinkedIn: [Siddhi Jadhav](https://www.linkedin.com/in/siddhi-jadhav-1865a0259/)
* GitHub: [Siddhi-Jadhav01](https://github.com/Siddhi-Jadhav01)
