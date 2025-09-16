import streamlit as st

st.set_page_config(page_title="Civic Complaint Portal", layout="centered")

st.title("Civic Complaint Readdressal Portal")
st.write("Welcome! Use this demo Streamlit app to submit a complaint.")

with st.form("complaint_form"):
    name = st.text_input("Your Name")
    department = st.selectbox("Department", ["Sanitation", "Water", "Electricity", "Other"])
    description = st.text_area("Complaint Description")
    submitted = st.form_submit_button("Submit Complaint")

if submitted:
    st.success(f"Thank you, {name}! Your complaint to {department} has been submitted.")
    st.write("**Complaint Details:**")
    st.write(description)
