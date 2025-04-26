import streamlit as st 
import pandas as pd  
from io import BytesIO 

st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")

st.title("📂 File Converter & Cleaner")
st.write("Upload your CSV and Excel Files to clean the data convert formats effortlessly🚀")

files= st.file_uploader("Upload CSV or Excel Files",type=["CSV","xlsx"],accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]

        df =pd.read_excel(file) if ext == "CSV" else pd.read_csv(file)

        st.subheader(f"🔍 {file.name} - preview")
        st.dataframe(df.head()) 

        if st.checkbox(f" Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True )
            st.success("Missing Values filled successfully")
            st.dataframe(df.head())

        selected_columns = st.multiselect(f" Select Coulumns , {file.name}",df.columns, default = df.columns)
        df = df [selected_columns]
        st.dataframe(df.head())

        if st.checkbox(f"📊 Show Chart - {file.name}")and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])


        format_choice =st.radio(f"Convert {file.name} to:",["CSV", "Excel"], key=file.name)

        if st.button(f"⬇ Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(ext, "xlsx")
            output.seek(0)
            st.download_button("⬇ Download File", file_name=new_name, data=output, mime=mime)
        st.success("Processing Completed!🚀")
# venv\Scripts\activate
# streamlit run g_m_s.py