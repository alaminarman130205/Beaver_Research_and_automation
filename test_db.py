
import streamlit as st
from database import test_connection

st.set_page_config(page_title="Database Connection Test")

st.title("Supabase PostgreSQL Connection Test")

if st.button("Test database connection", type="primary"):
    try:
        result = test_connection()
        st.success("Database connection successful!")
        st.write("Connected database:", result["database_name"])

    except Exception as e:
        st.error("Connection failed.")
        st.code(f"{type(e).__name__}: {e}")
