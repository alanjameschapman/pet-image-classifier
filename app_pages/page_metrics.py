import os
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
# from matplotlib.image import imread
from src.ml.evaluate_clf import load_test_evaluation


def page_metrics():
    '''Function to display the model metrics page'''

    version = 'v5'
    base_dir = os.path.dirname((os.path.dirname(__file__)))
    outputs = os.path.join(base_dir, f'outputs/{version}')

    st.header("Model Metrics")

    st.write("Train, Validation and Test Set: Labels Frequencies")

    st.image((f"{outputs}/images_per_dir.png"), caption="Number of images per directory")

    st.write('The median is around 160 images per breed, with a range of around 100-230 images. '
    'Outliers are saved in the `outlier_dirs.pkl` file and can be removed if training bias is identified.')
    
    st.write("---")

    st.header('Learning Curves')

    st.write('Learning curves show how the model learns with respect to accuracy and loss as it sees new data.'
    ' The aim is to have training and validation curves which converge over time. ')

    st.image((f"{outputs}/learning_curve_tuned_acc.png"), caption="Training accuracy")

    st.write('The training accuracy curves converged at around 80% and there are no fluctuations or divergences.'
    'We can therefore conclude that the model has not overfitted and should perform well on unseen test data.')

    st.image((f"{outputs}/learning_curve_tuned_loss.png"), caption="Training loss")

    st.write('The training loss curves converged at around 0.75 and there are no fluctuations or divergences.'
    'We can therefore conclude that the model has not overfitted and should perform well on unseen test data.')

    st.write("---")

    st.header("Generalised Performance on Test Set")

    # Loading and displaying test set evaluation metrics (loss and accuracy)
    evaluation = load_test_evaluation(version)
    df_evaluation = pd.DataFrame(evaluation, index=['Accuracy', 'Loss'])
    st.dataframe(df_evaluation)

    st.write('The model has an accuracy and loss of around 83% and 0.75 respectively. An accuracy of 83% '
    'tells us that the model is good at predicting on unseen test data. Coupled with the dashboard giving three'
    'top predictions based on accuracy, this value should be ample for our purposes. The loss tells us how far'
    'the predicted values deviate from the actual values and 0.75 can be considered good for classification '
    'with 120 classes.')

    st.write("---")
