# 🌤️ IoT Weather Prediction System 

This project is a comprehensive end-to-end IoT-based weather prediction and smart irrigation monitoring system that integrates real-time environmental sensing with machine learning–based weather forecasting. At its core is the ESP8266 NodeMCU microcontroller, which collects live data from a set of sensors, including the DHT11 for temperature and humidity, the BMP180 for atmospheric pressure, and a soil moisture sensor to monitor ground conditions.

The sensor data is transmitted over Wi-Fi to a lightweight Flask-based backend API running on the same local network. This backend is equipped with a pre-trained machine learning model that processes the input (including a calculated dew point and fixed values for wind speed and visibility) to accurately predict the current weather condition (e.g., Sunny, Rainy, Cloudy). The model was trained using scikit-learn and uses a scaler and label encoder for consistent prediction behavior.

Once the Flask API returns a prediction, the ESP8266 updates the Blynk IoT app, displaying real-time values for temperature, humidity, pressure, soil moisture, and the predicted weather condition. This app serves as a live dashboard for users to monitor environmental parameters remotely.

A key feature of the system is the ability for users to manually control a water pump based on informed decision-making. The pump is not automated—instead, the user reviews the current soil moisture level and weather prediction via the Blynk app and decides whether or not to activate the pump using a control button. For example, if the soil appears dry but rain is predicted, the user may choose to delay watering to conserve water resources.

Overall, this project showcases the effective integration of IoT hardware, machine learning, and cloud-connected mobile apps to support smarter and more sustainable irrigation practices. It provides a real-world application of predictive analytics in agriculture and smart gardening, combining accessible components with practical functionality.

---

## 📌 System Overview

[Sensors]
(collect real-time temperature, humidity, pressure)
↓
[ESP8266]
→ Sends data to Flask API
← Receives predicted weather condition
→ Sends temperature, humidity, pressure + prediction to Blynk app
→ User manually controls water pump based on
 Soil moisture reading,
 Predicted weather (e.g., avoid watering if rain is predicted)

## 🧠 How the Code Works

### 🛰️ Arduino code for ESP8266

- **Reads sensor data**:
  - Temperature and humidity from DHT11 (connected to D4)
  - Pressure from BMP180 (connected to I2C pins)
  - Soil moisture level from analog pin A0
- **Displays sensor values on Blynk App** via virtual pins.
- **Sends a POST request** to the Flask API `/predict` endpoint with:
  ```json
  {
    "temperature": 30,
    "humidity": 65,
    "pressure": 100.8
  }
-Receives the predicted weather condition from Flask API (e.g., "Rainy")

-Displays prediction on Blynk (V4)

-Controls the water pump: If soil is dry and no rain is predicted, the user can turn on the pump .Otherwise,he can keep the pump off

🌐 Example API Request
Request:


{

  "temperature": 29.5,
  
  "humidity": 72,
  
  "pressure": 100.8
  
}
