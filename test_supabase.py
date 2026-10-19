
import streamlit as st
from supabase import create_client

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_SECRET_KEY"]

supabase = create_client(url, key)

# Read only the table metadata through a harmless query.
# This does not insert or modify any client information.
result = (
    supabase
    .table("client_inquiries")
    .select("id")
    .limit(1)
    .execute()
)

print("Supabase connection successful.")
print("Query returned", len(result.data), "row(s).")
