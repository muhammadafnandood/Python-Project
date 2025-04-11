import re
import streamlit as st
def  check_password_strength(password):
    score = 0
    #length check
    if len(password) >= 8:
     score += 1

    #Uppercase letters
    if re.search(r'[A-Z]',password):
       score +=1

    # Lowercase Letters
    if re.search(r'[a-z]', password):
        score += 1

# Numbers
    if re.search(r'[0-9]', password):
        score += 1
   
    #Special characters
    if re.search(r'[\W_]',password):
       score += 1

    #Result based on score
    if score <= 2:
         st.success("Local password")
         return"🔴 Weak"
    elif score == 3: 
       st.success("Random password")
       return "🟠 Medium"
    elif score == 4:
      st.success("Good")
      return "🟡 Strong"

    elif score == 5:
       st.success("wounderful password")
       return "🟢 Very Strong"

#Streamlit UI
st.title("🔐 Password Strength Checker")
password =st.text_input("Enter your password:",type="password")
if password: 
   strength  = check_password_strength(password)
   st.markdown(f"### Password Strength: **{ strength}**")

button = st.button("Enter")
