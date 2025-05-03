import streamlit as st
import numpy as np
import pickle
import os
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

scaler_path = r"C:\Users\User\Downloads\scaler.pkl"
model_path = r"C:\Users\User\Downloads\model.h5"

def main1():
    st.title('Fuel Efficiency Prediction')

    

    cylinders = st.slider("Enter number of cylinders",3,8,5,step=1)
    displacement = st.number_input("Displacement",60,500,step=1)
    horsepower = st.number_input("Horsepower",40,300,100,step=1)
    weight = st.number_input("Weight",1600,5200,step=1)
    acceleration = st.number_input("Acceleration",8,30)
    model_year = st.number_input("Model Year",step=1)
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
    if st.button('Predict Efficiency'):
        prediction = model.predict(values_scaled)

        st.success("Fuel Efficiency of your car is:{}".format( prediction[0]))


if __name__ == '__main__':
    main1()
