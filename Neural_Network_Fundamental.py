import tensorflow as tf
from tensorflow import keras
import numpy as np

# Training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [1]])

# Create Neural Network
model = keras.Sequential([
    keras.layers.Dense(4, activation='relu', input_shape=(2,)),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Predict output
prediction = model.predict(np.array([[1, 1]]), verbose=0)

print("Predicted Output:", prediction)

print("Predicted Output:", prediction)
