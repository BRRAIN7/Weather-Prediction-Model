import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib


# Load the dataset
file_path = 'D:\\Arnav\\SYMBIOSIS\\PROJECTS\\MLM\\Data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Handle missing values
imputer = SimpleImputer(strategy='mean')
data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']] = imputer.fit_transform(
    data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']])

# Encode the target variable (Weather)
label_encoder = LabelEncoder()
data['Weather'] = label_encoder.fit_transform(data['Weather'])

# Extract features and target
X = data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']]
#X = data[['Temp_C', 'Rel Hum_%', 'Press_kPa']]
y = data['Weather']

# Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Get unique classes in y_test
unique_classes = np.unique(y_test)

# Classification report using only the classes present in the test set
print(classification_report(y_test, y_pred, target_names=label_encoder.inverse_transform(unique_classes), labels=unique_classes))

joblib.dump(rf_model, 'weather_prediction_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

