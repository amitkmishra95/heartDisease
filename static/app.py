import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pre-trained model
model = None
with open('E://model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set the title of the app
st.title("Heart Disease Prediction")

# User inputs
age = st.number_input("Enter Your Age", min_value=1, max_value=120, value=30, step=1)
chest_pain = st.selectbox("Chest Pain Type (0-3)", options=["", "Typical Angina (0)", "Atypical Angina (1)", "Non-anginal Pain (2)", "Asymptomatic (3)"])
max_heart_rate = st.number_input("Enter Your Max Heart Rate", min_value=50, max_value=220, value=120, step=1)

# When the user clicks the "Predict" button
if st.button("Predict"):
    if chest_pain == "":
        st.error("Please select a chest pain type.")
    else:
        # Map the chest pain type to numeric values
        chest_pain_map = {
            "Typical Angina (0)": 0,
            "Atypical Angina (1)": 1,
            "Non-anginal Pain (2)": 2,
            "Asymptomatic (3)": 3
        }
        chest_pain_value = chest_pain_map.get(chest_pain, -1)

        # Create a DataFrame for prediction
        user_data = pd.DataFrame([[age, chest_pain_value, max_heart_rate]], columns=['age', 'cp', 'thalach'])

        # Make prediction
        try:
            prediction = model.predict(user_data)
            result = "Heart Disease Present" if prediction[0] == 1 else "No Heart Disease"
            st.success(f"Prediction: {result}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

