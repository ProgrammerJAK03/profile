import streamlit as st
from db import fetch_user
import base64
from io import BytesIO

st.title("👤 User Profile")

user = fetch_user()

if user:
    name, phone, image = user

    try:
        # Convert base64 to image bytes
        image_bytes = base64.b64decode(image)
        image_file = BytesIO(image_bytes)

        # Display image
        st.image(image_file, width=150)
    except:
        st.warning("Image could not be loaded.")

    st.write("**Name:**", name)
    st.write("**Phone:**", phone)
else:
    st.warning("No user data found.")

