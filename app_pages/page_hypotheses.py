import streamlit as st


def page_hypotheses():
    '''Function to display the hypotheses page'''

    st.header("Hypotheses, validations and results")

    st.markdown('''
    | Hypothesis | Validation | Result |
    | :- | :- | :- |
    | The chosen dataset of dog images is representative of the breeds that the consultants will encounter in-consult. | The dataset will be reviewed by the client. | The client was satisfied that the dataset was suitable. |
    | A Convolutional Neural Network (CNN) can be trained on the dataset to accurately predict the breed based on a new and unseen image. | The model can accurately predict the breed(s) of an unseen image. | Two different datasets were trialled for model training. One with ca. 30 images per breed, another with ca. 150 images. The latter performed better, but still required transfer learning i.e. using a pre-trained base model to produce sufficient results.  |
    | The model can predict the breed of dog with 95% accuracy | The model will be evaluated on a test set of images to determine its accuracy in predicting the breed. The results will be displayed on a dashboard. | The best accuracy achieved was around 80%. Whilst this failed to meet the 95% target, it was enough to provide the functionality required by the client of providing the top 3 breeds based on probability. |
    | The model can predict the top 3 breeds the image may belong to. | The top 3 breeds are displayed according to model certainty. | The model provides the functionality required by the client of providing the top 3 breeds based on certainty. |
    ''')