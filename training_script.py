# model/training_script.py
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Sample dataset
data = {
    'symptoms': [
        "fever cough sore throat",
        "headache nausea vomiting",
        "chest pain shortness of breath",
        "sneezing runny nose",
        "stomach ache diarrhea",
    ],
    'diseases': [
        ["flu"],
        ["migraine"],
        ["heart attack"],
        ["common cold"],
        ["food poisoning"]
    ]
}

df = pd.DataFrame(data)

# Vectorize symptoms
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['symptoms'])


mlb = MultiLabelBinarizer()
y = mlb.fit_transform(df['diseases'])

# Train model
model = MultinomialNB()
model.fit(X, y)

with open("symptom_model.pkl", "wb") as f:
# Save model, vectorizer, and label encoder
    pickle.dump((model, vectorizer, mlb), f)

print("Model trained and saved as symptom_model.pkl")
