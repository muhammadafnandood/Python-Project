import streamlit as st


units = {
    "meters": 1,
    "kilometers": 1000,
    "centimeters": 0.01,
    "millimeters": 0.001,
    "inches": 0.0254,
    "feet": 0.3048
}

# Input from user
value = st.number_input("Enter the value:")
from_unit = st.selectbox("Convert from:", list(units.keys()))
to_unit = st.selectbox("Convert to:", list(units.keys()))

# Perform conversion
result = value * units[from_unit] / units[to_unit]

# Display result
st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
 
category = st.button( "Convert")
category = st.success("Good")