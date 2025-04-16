const fs = require('fs');
const path = require('path');

// Correct relative path
const modelPath = path.join(__dirname, 'model.json');

let symptomModel = {};

fs.readFile(modelPath, 'utf8', (err, data) => {
  if (err) {
    console.error("Failed to load model.json:", err);
    return;
  }

  try {
    symptomModel = JSON.parse(data);

    // Prediction test after loading
    const userSymptoms = "fever, cough, headache";
    const diagnosis = predictDisease(userSymptoms);
    console.log("Prediction:", diagnosis);
  } catch (parseErr) {
    console.error("Error parsing model.json:", parseErr);
  }
});

function predictDisease(inputSymptoms) {
  const inputKey = inputSymptoms.toLowerCase().split(',').map(s => s.trim()).sort().join(",");
  const result = symptomModel[inputKey];
  return result || "Sorry, no matching disease found.";
}