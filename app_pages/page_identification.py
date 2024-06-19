import streamlit as st
# from PIL import Image
# import numpy as np
# import pandas as pd

# from src.ml.predictive_analysis import (
#     load_model_and_predict,
#     resize_input_image,
#     plot_probabilities
# )


# def page_identification():
#     '''Function to display the breed identification page'''

#     st.write('You can download the dataset for live prediction here:')

#     st.write("---")

#     images_buffer = st.file_uploader(f'Upload cherry leaves images. You may '
#                                      f'select more than one.',
#                                      type=['png', 'jpg'],
#                                      accept_multiple_files=True)

#     if images_buffer is not None:
#         df_report = pd.DataFrame([])
#         for image in images_buffer:

#             img_pil = (Image.open(image)).convert('RGB')
#             st.info(f"Cherry Leaf Image: **{image.name}**")
#             img_array = np.array(img_pil)
#             st.image(img_pil,
#                      caption=f"Image Size: {img_array.shape[1]}px width "
#                              f"x {img_array.shape[0]}px height")

#             version = 'v2'
#             resized_img = resize_input_image(img=img_pil, version=version)
#             pred_proba, pred_class = load_model_and_predict(resized_img,
#                                                             version=version)
#             plot_probabilities(pred_proba, pred_class)

#             df_report = df_report.append({"Name": image.name,
#                                           'Result': pred_class},
#                                          ignore_index=True)
