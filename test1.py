import streamlit as st
st.header("shrikansh bmi calculator")
name = st.text_input("enter your name")
age = st.number_input("enter your age", min_value=0, max_value=150  )
height = st.number_input("enter your height in cm", min_value=0.0, max_value=300.0)
weight = st.number_input("enter your weight in kg", min_value=0.0,  max_value=500.0)
gender = st.selectbox("select your gender", ("male", "female")) 
if st.button("calculate bmi"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"{name}, your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese get of the macdonalds and do some workout.")
    else:
        st.write("Please enter a valid height greater than 0.")