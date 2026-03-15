import streamlit as st
import pickle

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

st.title("Fake News Detector")

news = st.text_area("Enter News Text")

if st.button("Predict"):
    vec = vectorizer.transform([news])
    prediction = model.predict(vec)

    if prediction[0] == 0:
        st.error("Fake News")
    else:
        st.success("Real News")
