import numpy as np
from flask import Flask, request, jsonify
import joblib

# Load the trained model (ensure this is the correct path to your saved model)
model = joblib.load('model/model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "ML Model API is running!"

# Define a route for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the POST request
        data = request.get_json(force=True)

        # Extract id_cycle and Temperature_measured from the input JSON
        id_cycle = data['id_cycle']
        temperature_measured = data['Temperature_measured']

        # Create the input array for the model (matching the feature order during training)
        input_features = np.array([[id_cycle, temperature_measured]])

        # Predict using the loaded model
        prediction = model.predict(input_features)

        # Return the prediction result as a JSON response
        return jsonify({'predicted_capacity': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
