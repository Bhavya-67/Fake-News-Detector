import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model/model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

st.title("Fake News Detector")
st.write("Enter a news article to check if it is Fake or Real.")

news = st.text_area("Enter News Text")

if st.button("Predict"):

    vectorized_text = vectorizer.transform([news])

    prediction = model.predict(vectorized_text)

    if prediction[0] == 0:
        st.error("This News is Fake")
    else:
        st.success("This News is Real")
