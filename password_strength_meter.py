import re
import streamlit as st
def password_strength(password):

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[A-Z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()_+-=,.?\":{}|<>]", password) is None


    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score <= 2: 
         return "🔴 Weak"
    elif score == 3:
         return "🟠 Moderate"
    
    else:
         return "🟢 Strong"
    

    # streamlit UI
st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:",type ="password")
          

if password:
    
     result = password_strength(password)
     st.markdown(f"### Password Strength: **{result}**")
st.success( "Good")
st.button("Enter")





