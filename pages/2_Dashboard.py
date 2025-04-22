import streamlit as st
from db import update_user, fetch_user
import base64

st.title("🛠️ Dashboard - Edit User Info")

user = fetch_user()

if user:
    old_name, old_phone, old_image = user
else:
    old_name = old_phone = old_image = ""

with st.form("user_form"):
    name = st.text_input("Name", old_name)
    phone = st.text_input("Phone Number", old_phone)

    # 👇 Image uploader
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("Save")

    if submitted:
        if uploaded_file is not None:
            # Convert uploaded file to base64
            image_data = uploaded_file.read()
            encoded_image = base64.b64encode(image_data).decode("utf-8")
        else:
            # If no new image is uploaded, keep old one
            encoded_image = old_image

        update_user(name, phone, encoded_image)
        st.success("User data updated successfully!")

