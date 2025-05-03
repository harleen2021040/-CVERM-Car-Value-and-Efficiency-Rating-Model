import streamlit as st
from predict_page import main
from predict_efficiency_page import main1
st.title('CVERM(Car Value and Efficiency Rating Model)')

st.write("""### Lets make selling cars EASIER""")

page = st.sidebar.selectbox("Car Value Prediction OR Fuel Efficiency Prediction",("Car Value","Fuel Efficiency"))

if page == "Car Value":
    main()
else:
    main1()