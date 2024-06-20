import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


from src.ml.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    # plot_probabilities
)


def page_identification():
    '''Function to display the breed identification page'''

    st.write('You can download the dataset for live prediction here:')

    st.write("---")

    image_buffer = st.file_uploader('Upload image of dog to identify',
                                     type=['png', 'jpg', 'jpeg'],
                                     accept_multiple_files=False) # was True

    if image_buffer is not None:
        img_pil = (Image.open(image_buffer)).convert('RGB')
        st.info(f"Uploaded dog image: **{image_buffer.name}**")
        st.image(img_pil,
                caption=f"Image Size: {img_pil.size[0]}px width "
                        f"x {img_pil.size[1]}px height")

        resized_img = resize_input_image(img=img_pil)

        # st.image(resized_img,
        #         caption=f"Resized Image Size: {resized_img.size[0]}px width "
        #                 f"x {resized_img.size[1]}px height")

        version = 'v5'

        predictions = load_model_and_predict(resized_img, version=version)

        # Print the top 3 predictions
        st.text(f'Normalized predictions: {predictions}')
        
        # plot_probabilities(pred_proba, pred_class)

        # df_report = df_report.append({"Name": image.name,
        #                               'Result': pred_class},
        #                              ignore_index=True)
