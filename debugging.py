import os

# Check if the model file exists
model_path = 'C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/model.h5'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"The model file at {model_path} was not found.")

# Load the trained model
model = tf.keras.models.load_model(model_path)
