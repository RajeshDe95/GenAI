from sqlalchemy import null
import streamlit as st

def pdf_uploader():
    st.title("pdf Uploader")
    Uploaded_file = st.file_uploader("Choose a pdf files", accept_multiple_files=True,type="pdf")
    if Uploaded_file is not None:
        st.success("File uploaded Successfully")
    else:
        st.warning("Please upload a pdf file")

    return Uploaded_file
