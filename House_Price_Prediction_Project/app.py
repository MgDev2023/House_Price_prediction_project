import streamlit as st
import numpy as np
import joblib

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

median_income = st.number_input("Median Income")
housing_median_age = st.number_input("Housing Median Age")
total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")

features = np.array([[median_income, housing_median_age, total_rooms,
                      total_bedrooms, population, households,
                      latitude, longitude]])

if st.button("Predict Price"):
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")