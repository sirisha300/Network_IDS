import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load the preprocessed data
data = pd.read_csv('C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/capture_processed.csv')

# Assume 'proto' is the target variable for classification
X = data.drop(columns=['proto'])
y = data['proto']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_dim=X_train.shape[1], activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy}')
