

import streamlit as st

# 🎨 Stylish      Title and Subtitle
st.markdown("## 🌈✨ Welcome to the Ultimate Unit Converter ✨🌈")
st.caption("Easily convert between popular length units with style 🚀")

# ➖ Divider for Clean Look
st.markdown("---")

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

# Display result on button click
if st.button("Convert"):
    st.success(f"{value} {from_unit} is equal to {result} {to_unit}")









