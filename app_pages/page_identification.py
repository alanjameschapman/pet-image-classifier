import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


from src.ml.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
)


def page_identification():
    '''Function to display the breed identification page'''

    st.header('Upload your image below to identify the breed.')

    image_buffer = st.file_uploader(label='Image uploader', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)

    if image_buffer is not None:
        img_pil = (Image.open(image_buffer)).convert('RGB')
        st.info(f"Uploaded dog image: **{image_buffer.name}**")
        st.image(img_pil,
                caption=f"Image Size: {img_pil.size[0]}px width "
                        f"x {img_pil.size[1]}px height")

        resized_img = resize_input_image(img=img_pil)

        version = 'v5'

        predictions = load_model_and_predict(resized_img, version=version)

        # Print the top 3 predictions
        st.write('Normalised predictions for this image, in descending order of certainty are:')

        st.text('\n'.join(predictions))
