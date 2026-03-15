import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocess import clean_text

# Load datasets
fake = pd.read_csv("dataset/Fake_small.csv")
true = pd.read_csv("dataset/True_small.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake,true])

# Clean text
data["text"] = data["text"].apply(clean_text)

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english")

X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()

model.fit(X_vectorized,y)

# Save model
pickle.dump(model,open("model/model.pkl","wb"))
pickle.dump(vectorizer,open("model/vectorizer.pkl","wb"))

print("Model trained successfully")
