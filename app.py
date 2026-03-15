import streamlit as st
import base64

def set_bg():
    with open("background.jpeg", "rb") as file:
        data = file.read()
        encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

st.title("📰 Fake News Detector")

news = st.text_area("Enter News Text")

if st.button("Check News"):
    st.success("Prediction will appear here")
