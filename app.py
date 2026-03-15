import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.title("Fake News Detector")

# Load dataset
fake = pd.read_csv("dataset/Fake_small.csv")
true = pd.read_csv("dataset/True_small.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

X = data["text"]
y = data["label"]

# Train model
vectorizer = TfidfVectorizer(stop_words="english")
X_vector = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vector, y)

# User input
news = st.text_area("Enter news text")

if st.button("Predict"):
    vec = vectorizer.transform([news])
    prediction = model.predict(vec)

    if prediction[0] == 0:
        st.error("Fake News")
    else:
        st.success("Real News")
