import pandas as pd
import json

# Load the dataset
df = pd.read_csv('AI_Symptom_Checker_Dataset.csv')

# Preview your columns
print(df.columns)

# Assuming your dataset has multiple symptom columns and one disease column
# Replace these with your actual column names
symptom_columns = ['Patient ID', 'Age', 'Gender', 'Symptoms', 'Predicted Disease', 'Severity', 'Confidence Score']  # Example
disease_column = 'Disease'  # Replace with the actual name

lookup = {}

for _, row in df.iterrows():
    symptoms = [str(row[col]).lower().strip() for col in symptom_columns if pd.notna(row[col])]
    symptoms_key = ",".join(sorted(symptoms))
    disease = str(row[disease_column])
    lookup[symptoms_key] = disease

# Save the lookup as model.json
with open("model.json", "w") as f:
    json.dump(lookup, f, indent=2)

print("model.json created successfully!")