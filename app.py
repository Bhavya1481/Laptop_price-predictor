import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction App")

st.divider()

st.write("With this app after using the calculation button when you entered the values for all laptop specifications you can get a price estimation for your laptop")

st.divider()

# Create input fields for all required features
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Select Brand", options=[0, 1, 2], format_func=lambda x: ["Brand 0", "Brand 1", "Brand 2"][x])
    processor_speed = st.number_input("Enter Processor Speed", value=2.50, step=0.50)
    ram_size = st.number_input("Enter RAM Size (GB)", value=16, step=8)

with col2:
    storage_capacity = st.number_input("Enter Storage Capacity (GB)", value=512, step=256)
    screen_size = st.number_input("Enter Screen Size (inches)", value=15.0, step=1.0)
    weight = st.number_input("Enter Weight (kg)", value=2.0, step=0.5)

st.divider()

prediction = st.button("Price Estimation Button!")

st.divider()

if prediction:
    # Create input data with all required features in the correct order
    input_data = pd.DataFrame({
        'Brand': [brand],
        'Processor_Speed': [processor_speed],
        'RAM_Size': [ram_size],
        'Storage_Capacity': [storage_capacity],
        'Screen_Size': [screen_size],
        'Weight': [weight]
    })
    
    prediction = model.predict(input_data)
    st.write(f"The estimated price of your laptop is: **${prediction[0]:.2f}**")
else:
    st.write("Please enter the values for all laptop specifications to get a price estimation")