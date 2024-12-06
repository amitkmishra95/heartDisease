from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('template/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.json
    age = int(data['age'])
    chest_pain = int(data['chestPain'])  # Values should be between 0 to 3
    max_heart_rate = int(data['maxHeartRate'])

    # Ensure input values are within the expected range
    if not (0 <= chest_pain <= 3):
        return jsonify({'error': 'Invalid chest pain type!'}), 400

    # Prepare input for the model
    input_data = np.array([[age, chest_pain, max_heart_rate]])

    # Predict using the loaded model
    prediction = model.predict(input_data)[0]

    # Return the prediction result
    result = 'Heart Disease Present' if prediction == 1 else 'No Heart Disease'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)