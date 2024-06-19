import streamlit as st
from tensorflow import keras
import tensorflow as tf
import pickle
import numpy as np
# import pandas as pd
# import plotly.express as px
# from tensorflow.keras.models import load_model
from PIL import Image
# from typing import Tuple, Union, Literal
from src.data_management import load_pkl_file
# from tensorflow.keras.preprocessing.image import img_to_array


def resize_input_image(img: np.ndarray, version: str) -> np.ndarray:
    """
    Resize input image to image shape for model compatibility.
    """

    image_shape = (224, 224) # Image shape required by the model
    img_resized = img.resize(image_shape)
    my_image = np.expand_dims(img_resized, axis=0) # Add /255 if needed

    return my_image


def load_model_and_predict(resized_img: np.ndarray, version: str): # , class_names: list removed
    """
    Load and perform ML prediction on live images
    """

    model = keras.models.load_model(f'outputs/{version}/model_fine_tuned.keras')

    # Load the class names
    class_names = load_pkl_file(file_path=f"outputs/{version}/class_indices.pkl")

    # Predict the probabilities of each class for the selected image
    predictions = model.predict(resized_img)

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

