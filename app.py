from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('weather_prediction_model.pkl')  # Adjust the file path if needed
scaler = joblib.load('scaler.pkl')  # Adjust the file path if needed
label_encoder = joblib.load('label_encoder.pkl')  # Load the label encoder if saved

# Root route
@app.route('/')
def home():
    return "Welcome to the weather prediction API!"

# Favicon route to prevent 404 error for /favicon.ico
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Extract the sensor values from the JSON data
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    pressure = data.get('pressure')

    # Calculate the missing values
    dew_point = temperature - ((100 - humidity) / 5)  # Example calculation for dew point
    #pressure=100.8
    visibility = 10  # Default value for visibility
    wind_speed = 5   # Default value for wind speed

    # Check if any value is missing
    if None in [temperature, humidity, pressure]:
        return jsonify({"error": "Missing one or more sensor values"}), 400

    # Scale the input values
    features = np.array([[temperature, dew_point, humidity, wind_speed, visibility, pressure]])
    scaled_features = scaler.transform(features)
    
    # Make a prediction
    prediction = model.predict(scaled_features)

    # Decode the prediction using the LabelEncoder
    weather_condition = label_encoder.inverse_transform(prediction)

    # Return the weather condition as a JSON response
    return jsonify({"prediction": weather_condition[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Bind to all IP addresses on the local machine

