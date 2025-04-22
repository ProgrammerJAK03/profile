import streamlit as st
from db import update_user, fetch_user

st.title("🛠️ Dashboard - Edit User Info")

user = fetch_user()

if user:
    old_name, old_phone, old_image = user
else:
    old_name = old_phone = old_image = ""

with st.form("user_form"):
    name = st.text_input("Name", old_name)
    phone = st.text_input("Phone Number", old_phone)
    image = st.text_input("Image URL", old_image)
    submitted = st.form_submit_button("Save")

    if submitted:
        update_user(name, phone, image)
        st.success("User data updated successfully!")


