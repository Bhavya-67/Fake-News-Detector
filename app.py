import streamlit as st
import joblib
from preprocess import clean_text

# Load model
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.title("Fake News Detector")

st.write("Enter a news headline to check whether it is Fake or Real")

user_input = st.text_area("Enter News Text")

if st.button("Check News"):

    cleaned = clean_text(user_input)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    if prediction == "fake":
        st.error("This news is FAKE")
    else:
        st.success("This news is REAL")
