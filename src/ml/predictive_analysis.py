import streamlit as st
from tensorflow import keras
import tensorflow as tf
import pickle
import numpy as np
import os
# import pandas as pd
# import plotly.express as px
# from tensorflow.keras.models import load_model
from PIL import Image
# from typing import Tuple, Union, Literal
from src.data_management import load_pkl_file
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model


def resize_input_image(img): # : np.ndarray
    """
    Resize input image to image shape for model compatibility.
    """

    size = (224, 224) # Image shape required by the model
    # img_resized = img.resize(image_size)
    # my_image = np.expand_dims(img_resized, axis=0) # Add /255 if needed

    img = img.convert('RGB')  # Convert image to RGB mode

    img.thumbnail(size)

    # Crop the image to be 224x224
    width, height = img.size
    left = (width - 224)/2
    top = (height - 224)/2
    right = (width + 224)/2
    bottom = (height + 224)/2
    resized_image = img.crop((left, top, right, bottom))

    return resized_image


def load_model_and_predict(resized_img, version): # , class_names: list removed
    """
    Load and perform ML prediction on live images
    """
    
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    outputs = os.path.join(base_dir, f'outputs/{version}')

    model = load_model(f'{outputs}/model_fine_tuned.h5')

    # Load the class names
    class_names = load_pkl_file(file_path=f"{outputs}/class_names.pkl")

    # Convert the PIL image to a NumPy array and ensure it has the correct dimensions
    image_array = img_to_array(resized_img)
    resized_img_array = np.expand_dims(image_array, axis=0)

    # Predict the probabilities of each class for the selected image
    predictions = model.predict(resized_img_array)

    # Apply a softmax since our model returns logits
    predictions = tf.nn.softmax(predictions)

    # Get the top 3 predictions
    values, indices = tf.nn.top_k(predictions, k=3)

    # Normalize the top 3 probabilities so they sum to 1
    values = values / np.sum(values)

    # Get the top 3 class names and their normalized probabilities
    top_3_classes = [f"{class_names[index]}: {prob:.2f}" for index, prob in zip(indices[0], values[0])]

    return top_3_classes


# def plot_probabilities():
#     """
#     Plot prediction probability
#     """

#     st.write('Plotting prediction probability...')

