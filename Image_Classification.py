import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image
import os

# Streamlit app header

st.header('SDA Face Recognition')

# Define model path

model_path = 'gee/SDA_image_classify.keras'

# Check if model exists

if not os.path.exists(model_path):
    st.error(f"Model not found at path: {model_path}. Please check the path.")
else:
    # Load model
    model = tf.keras.models.load_model(model_path)

# List of categories (names)
data_cat = ['Afif', 'Idzuddin', 'Najihah', 'Sentia']

# Image dimensions
img_height = 180
img_width = 180

# Upload image through Streamlit's file uploader
image_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if image_file is not None:
    try:
        # Open image file and resize to target size
        image = Image.open(image_file).convert("RGB").resize((img_width, img_height))

        # Convert image to numpy array and scale pixel values
        img_arr = np.array(image) / 255.0  # Scale values to [0, 1]

        # Add batch dimension for prediction
        img_bat = np.expand_dims(img_arr, axis=0)

        # Make prediction
        predict = model.predict(img_bat)

        # Get the prediction score and convert to probabilities
        score = tf.nn.softmax(predict[0])
        
        
        # Define confidence threshold (e.g., 60%)
        confidence_threshold = 0.60

        # Get the maximum confidence score
        confidence = np.max(score)

        # Check if the confidence is below the threshold
        if confidence < confidence_threshold:
            st.write("The model is not confident enough to make a reliable prediction.")
        else:
            # Display image and prediction
            st.image(image_file, width=200)
            st.write(f'This is {data_cat[np.argmax(score)]}')
            st.write(f'With accuracy of {np.max(score) * 100:.2f}%')

    except Exception as e:
        st.error(f"Error processing the image: {e}")
