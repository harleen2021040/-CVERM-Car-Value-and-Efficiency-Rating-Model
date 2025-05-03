import streamlit as st
import pickle
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb
import warnings

model = open(r'C:\Users\User\model_car_pridiction.pkl','+rb') 
model = pickle.load(model)
def main():
    html_temp="""
    <div style = "background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center;>Car price prediction</h2>
    </div>
    """
    st.title('Car Value Prediction')

    

    #present_price= st.number_input('Enter the Present price of your car(IN LAKHS)',2.5,20.0,step=1.0,key="resent price of your car(IN LAKHS)")

    present_car_price= st.number_input('Enter the present Price of your car(IN LAKHS)',1.0,100.0,step=1.0,key='present_car_price')

    p2 = st.number_input("Kilometers Driven",1000,5000000,step=10,key="ilometers Driven")
    

    Fuel_Type=st.selectbox("Fuel Type",("Petrol","Diesel","CNG"))
    if Fuel_Type == "Petrol":
        p3 = 0
    elif Fuel_Type == "Diesel":
        p3 = 1
    elif Fuel_Type == "CNG":
        p3 = 2
    
    

    Seller_Type=st.selectbox("Seller Type",('Dealer', 'Individual'))
    if Seller_Type == "Dealer":
        p4 = 0
    elif Seller_Type == "Individual":
        p4 = 1
    

    Transmission=st.selectbox("Transmission",('Manual', 'Automatic'))
    if Transmission == "Manual":
        p5 = 0
    elif Transmission == "Automatic":
        p5 = 1
    

    p6=st.slider("Number of Owners the car previously had?",0,3)

    date_time = datetime.datetime.now()
    Age= st.number_input("In which year car was purchased?",1990,date_time.year)
    p7 = date_time.year - Age
    

    
    data_new = pd.DataFrame({
    'Present_Price':present_car_price,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    
    if st.button('Predict Value'):
        pred = model.predict(data_new)
        st.success("You can sell your car for {:.2f} lakhs ".format(pred[0]))
    


if __name__ == '__main__':
    main()