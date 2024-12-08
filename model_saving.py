import tensorflow as tf

# Example model saving (replace with your actual model)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_shape=(10,), activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.save('C:/Users/smedishetty1/OneDrive/Documents/Cyber_Projects/NIDS/model.h5')
