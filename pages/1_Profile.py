import streamlit as st
from db import fetch_user

st.title("👤 User Profile")

user = fetch_user()

if user:
    name, phone, image = user
    st.image(image, width=150)
    st.write("**Name:**", name)
    st.write("**Phone:**", phone)
else:
    st.warning("No user data found.")
