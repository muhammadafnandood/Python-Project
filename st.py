# import streamlit as st
# import pandas as pd 

import streamlit as st
# st.title("Welcome to my first website")
# st.header("Python")
# st.subheader("java")
# st.markdown( "I Love Coding")
# st.code("""for i in range (1,5,1):
#         print("hi")
#         """)


#  excel file ke liye ye code he
# import pandas as pd  # ye excel sheet add karne ka code he 

# # veriable dataset
# dataset = pd .read_csv( "code.py.csv")

# st.dataframe(dataset)


name = st.text_input( "Enter your name :")
fname = st.text_input( "Enter your Father name :")

adr = st.text_area("Enter your text:")

# c_data = st.selectbox ("Enter your class:", (1,2,3,4,5,6,7,,8,9,10))

c_data = st.selectbox("Enter your class:", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

button = st.button( "Done")
if button :
    st.markdown(f"""
    name : {name}
    father name : {fname}
     address : {adr}
    class : {c_data}

""")
