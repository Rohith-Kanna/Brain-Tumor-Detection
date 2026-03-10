import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model(
    "brain_tumor_mobilenet_fixed.keras",
    compile=False
)

print("Model loaded")

# Dummy input (1 image, correct shape)
dummy_image = np.random.rand(1, 224, 224, 3).astype(np.float32)

# Try prediction
output = model.predict(dummy_image)

print("Prediction output:", output)
