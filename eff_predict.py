import streamlit as st
import numpy as np
import pickle
import os
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

scaler_path = r"C:\Users\User\Downloads\scaler.pkl"
model_path = r"C:\Users\User\Downloads\model.h5"

def main():
    st.title('CVERM (Car Value and Efficiency Rating Model)')

    st.write("Let's make selling cars EASIER")

    cylinders = st.number_input("Enter number of cylinders")
    displacement = st.number_input("Displacement")
    horsepower = st.number_input("Horsepower")
    weight = st.number_input("Weight")
    acceleration = st.number_input("Acceleration")
    model_year = st.number_input("Model Year")
    origin = st.number_input("Origin")

    values = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])

    # Load the scaler
    sc = None
    with open(scaler_path, 'rb') as f:
        sc = pickle.load(f)

    # Scale the input values
    values_scaled = sc.transform(values)

    # Load the model
    model = load_model(model_path)

    # Make the prediction
    prediction = model.predict(values_scaled)

    st.write("Prediction:", prediction[0])


if __name__ == '__main__':
    main()
