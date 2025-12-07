import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Return Prediction", layout="centered")

st.title("🛍️ Customer Return Prediction")
st.write("Enter customer + product details below to estimate return probability.")

# Load trained pipeline
import joblib

MODEL_PATH = "return_ensemble_pipeline.joblib"
DEFAULT_PATH = "default_values.pkl"

pipeline = joblib.load(MODEL_PATH)
default_values = joblib.load(DEFAULT_PATH)


# UI Inputs
st.sidebar.header("Minimal Inputs")

age = st.sidebar.number_input("Age", min_value=15, max_value=100, value=30)
price = st.sidebar.number_input("Price", min_value=0.0, value=100.0, format="%.2f")
discount = st.sidebar.number_input("Discount", min_value=0.0, value=0.0, format="%.2f")
product_return_rate = st.sidebar.slider("Product Return Rate", 0.0, 1.0, 0.10)
quantity = st.sidebar.number_input("Quantity", min_value=1, max_value=100, value=1)
loyalty_program = st.sidebar.selectbox("Loyalty Program", ["Yes", "No", "Unknown"])

# Prepare input row
# The UI provides only minimal inputs
input_df = pd.DataFrame([{
    "age": age,
    "price": price,
    "discount": discount,
    "product_return_rate": product_return_rate,
    "quantity": quantity,
    "loyalty_program": loyalty_program
}])

# ================================
# ADD DEFAULT VALUES FOR MISSING FEATURES
# ================================


# Add default values for missing columns
for col, val in default_values.items():
    if col not in input_df.columns:
        input_df[col] = val


st.subheader("📥 Input Data Preview")
st.write(input_df)

# Prediction
if st.button("Predict Return Probability"):
    try:
        pred = pipeline.predict(input_df)[0]
        proba = pipeline.predict_proba(input_df)[0][1]

        st.subheader("📊 Prediction Output")
        st.write(f"**Prediction:** {'Returned (1)' if pred == 1 else 'Not Returned (0)'}")
        st.write(f"**Return Probability:** {proba:.2f}")

        if pred == 1:
            st.error(f"⚠️ High Risk of Return — Probability = {proba:.2f}")
        else:
            st.success(f"✅ Low Risk of Return — Probability = {proba:.2f}")

    except Exception as e:
        st.error("Prediction failed: " + str(e))
