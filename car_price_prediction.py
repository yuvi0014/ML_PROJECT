import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st

def main():

    html_temp ="""<h1> Car Price Prediction</h1>"""
   
    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")

    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("this app will help you predict car selling Price.")
    
    p1=st.number_input("Enter the ex-showroom price (in lakhs):", 2.5,25.0, step=1.0)

    p2=st.number_input("Enter the car Driven(in thousands):", 100, 500000, step=100)
    
    s1=st.selectbox("Select the fuel type:", ["Petrol", "Diesel", "CNG", "Electric"])   
    if s1 == "Petrol":
        p3 = 0
    elif s1 == "Diesel":
        p3 = 1
    elif s1 == "CNG":
        p3 = 2
    elif s1 == "Electric":
        p3 = 3
    
    s2=st.selectbox("Select the seller type:", ["Individual", "Dealer", "Trustmark Dealer"])
    if s2 == "Individual":
        p4 = 0
    elif s2 == "Dealer":
        p4 = 1
    elif s2 == "Trustmark Dealer":
        p4 = 2
   
    s3=st.selectbox("Select the transmission type:", ["Manual", "Automatic"])
    if s3 == "Manual":
        p5 = 0
    elif s3 == "Automatic":
        p5 = 1

    p6 = st.slider("how many owners", 0, 3)
    date_time= datetime.datetime.now()
    years=st.number_input("car purchase year",1990,date_time.year, step=1)
    p7 = date_time.year - years
    data_now=pd.DataFrame ([{
        'Present_price':p1,
        'kms_Driven':p2,
        'Fuel_type':p3,
        'Seller_type':p4,
        'Transmission':p5,
        'Owner':p6,
        'Age':p7
    }],index=[0])

    if st.button("Predict"):
        try:
            pred = model.predict(data_now)
            st.success("you can sell your car at {:.2f} lakhs".format(pred[0]))
        except Exception as e:
            st.error("Something went wrong while predicting: {}".format(e))




if __name__ == '__main__':
    main()
