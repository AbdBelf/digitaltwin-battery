# Exporting a Trained Machine Learning Model and Deploying with a REST API

This guide shows how to:
- Export a trained machine learning model using `joblib` or `pickle`.
- Deploy the model using a simple REST API with Flask.

---

## 1. Exporting the Model

You can export your trained machine learning model in Python using `joblib` or `pickle`. This allows you to save the model to a file and load it later for predictions or deployment.

### Requirements

Install the necessary dependencies:

```bash
pip install joblib scikit-learn
```

###  Using joblib (Recommended)
joblib is more efficient than pickle for saving and loading large models, especially those that contain large NumPy arrays.

### Save the Model

```bash
import joblib

# Assuming your trained model is stored in a variable called `model`
joblib.dump(model, 'model.pkl')
```

### Load the Model
```bash
import joblib

# Load the model from the file
model = joblib.load('model.pkl')
```

##  2. Deploying the Model Using Flask (REST API)
Now that you’ve exported the model, you can deploy it using a REST API with Flask.

Flask App to Serve Predictions
Create a simple REST API that loads the model and serves predictions based on input features (id_cycle and Temperature_measured).

Requirements
Install Flask and any other required libraries: pip install Flask joblib numpy

## Python Script
Save the following as app.py:

```bash

import numpy as np
from flask import Flask, request, jsonify
import joblib

# Load the trained model (ensure this is the correct path to your saved model)
model = joblib.load('battery_capacity_model.pkl')

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
```

## Running the Flask App

```bash
python app.py
```

## Test the API

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"id_cycle": 100, "Temperature_measured": 30}'
```

## Example response

```bash
{
    "predicted_capacity": 1.75
}
```


## Deploying to a Simple HTTP Server

### Local Development
For simple deployment, you can use Flask’s built-in server by running the app directly with:

```bash
python app.py
```

This will serve the app at http://127.0.0.1:5000/.

### Production Deployment (Optional)

For production, you can use gunicorn to run the Flask app with multiple workers for better performance:

```bash
pip install gunicorn
gunicorn -w 4 app:app
```

#### What is gunicorn?
gunicorn (Green Unicorn) is a pre-fork worker model, meaning it forks multiple worker processes to handle requests. This is ideal for production environments where you need to handle multiple client requests efficiently. Flask’s built-in server is not designed for production as it can only handle one request at a time and isn't highly performant or secure.

#### Installation
First, install gunicorn if you haven’t already:

```bash
pip install gunicorn
```

After installing gunicorn, you can run your Flask app by executing the following command: 

```bash
gunicorn -w 4 app:app
```

This command tells gunicorn to serve your Flask app with 4 worker processes. Here’s a breakdown of the command:

gunicorn: The command to start the gunicorn server.
-w 4: This option specifies the number of worker processes. In this case, it tells gunicorn to use 4 workers, meaning 4 processes will handle requests concurrently. You can adjust the number based on the resources of your server (CPU cores) and the expected traffic.
app:app: This refers to your Flask application.
The first app is the name of the Python file (without the .py extension) where your Flask app is defined. For example, if your script is named app.py, then the first app refers to the file.
The second app is the name of the Flask app instance in your script. In the script, this would be:
