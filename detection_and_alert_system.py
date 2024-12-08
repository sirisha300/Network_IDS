from flask import Flask, request, jsonify
import pandas as pd
import tensorflow as tf
import ipaddress
import os

app = Flask(__name__)

# Define the model path
model_path = 'C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/model.h5'

# Check if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"The model file at {model_path} was not found.")

# Load the trained model
model = tf.keras.models.load_model(model_path)

def preprocess_data(data):
    try:
        # Convert IP addresses to integers
        data['src'] = data['src'].apply(lambda x: int(ipaddress.IPv4Address(x)))
        data['dst'] = data['dst'].apply(lambda x: int(ipaddress.IPv4Address(x)))

        # Normalize 'time' and 'length'
        data['time'] = (data['time'] - data['time'].min()) / (data['time'].max() - data['time'].min())
        data['length'] = (data['length'] - data['length'].min()) / (data['length'].max() - data['length'].min())

        return data
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        raise

@app.route('/detect', methods=['POST'])
def detect():
    try:
        data = request.json
        print(f"Received data: {data}")  # Debug: Print incoming data
        if data is None:
            raise ValueError("No JSON data received")
        
        df = pd.DataFrame([data])
        
        # Preprocess the input data
        df = preprocess_data(df)
        
        prediction = model.predict(df)
        print(f"Prediction: {prediction}")  # Debug: Print prediction
        
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        print(f"Error: {e}")  # Debug: Print any errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
