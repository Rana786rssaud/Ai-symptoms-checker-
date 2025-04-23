import pickle

# Load model and tools
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

def predict_disease(symptoms: list):
    input_text = ' '.join(symptoms)
    X = vectorizer.transform([input_text])
    pred = model.predict(X)
    return le.inverse_transform(pred)[0]

# Example usage
if __name__ == "__main__":
    user_symptoms = ["fever", "cough", "sore_throat"]
    prediction = predict_disease(user_symptoms)
    print("Predicted Disease:", prediction)
