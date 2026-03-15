import streamlit as st
import base64

with open("background.jpeg", "rb") as img:
    data = img.read()
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

st.title("📰 Fake News Detector")

news = st.text_area("Enter News Text")

if st.button("Check News"):
    st.write("Prediction will appear here")
