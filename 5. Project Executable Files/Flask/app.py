
import streamlit as st
import pickle

# Load model
model = pickle.load(open("final.pkl", "rb"))

st.title("E-commerce Shipping Prediction")

# User inputs
cost = st.number_input("Cost of the Product")
weight = st.number_input("Weight in gms")
discount = st.number_input("Discount offered")
calls = st.number_input("Customer Care Calls", step=1, min_value=0)

# Predict
if st.button("Predict"):
    X = [[cost, weight, discount, calls]]
    prediction = model.predict(X)
    st.success(f"Prediction: {prediction[0]}")
