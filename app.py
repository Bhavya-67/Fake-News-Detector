import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ---------- Background Style ----------
st.markdown("""
<style>
.stApp {
background: linear-gradient(to right, #141e30, #243b55);
color: white;
}

h1 {
text-align: center;
color: #f5f5f5;
}

textarea {
background-color: #1f2c3c !important;
color: white !important;
}

.stButton>button {
background-color: #ff4b4b;
color: white;
font-size: 18px;
border-radius: 10px;
height: 3em;
width: 150px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("📰 Fake News Detector")

st.write("Paste a news article below and the AI model will predict whether it is **Real or Fake**.")

# ---------- Load dataset ----------
fake = pd.read_csv("dataset/Fake_small.csv")
true = pd.read_csv("dataset/True_small.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

X = data["text"]
y = data["label"]

# ---------- Train Model ----------
vectorizer = TfidfVectorizer(stop_words="english")
X_vector = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vector, y)

# ---------- User Input ----------
news = st.text_area("Enter News Text")

if st.button("Predict"):

    vec = vectorizer.transform([news])
    prediction = model.predict(vec)

    if prediction[0] == 0:
        st.error("⚠ Fake News Detected")
    else:
        st.success("✅ This News Looks Real")
