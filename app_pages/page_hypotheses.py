import streamlit as st


def page_hypotheses():
    '''Function to display the hypotheses page'''

    st.title("Hypothesese, validations and results")

    st.header("Hypothesis 1")

    st.write('The chosen dataset of images of animals is representative of the animals that the consultants will encounter in practice')

    st.write('The dataset will be reviewed to ensure that it contains a diverse range of animals that the consultants may encounter in practice.')

    st.write('Client was satisfied that the dataset was not deficient in any other animal that was commonly seen during consults.')

    # st.markdown('| Hypothesis | Validation | Result |'
    #             '| :- | :- | :- |'
    #             '| The chosen dataset of images of animals is representative of the animals that the consultants will encounter in practice | The dataset will be reviewed to ensure that it contains a diverse range of animals that the consultants may encounter in practice. | Client was satisfied that the dataset was not deficient in any other animal that was commonly seen during consults. |'
    #             '| A Convolutional Neural Network (CNN) can be trained on the dataset of images of animals to accurately predict the animal based on a new and unseen image | The model can accurately predict the breed of an unseen image. | Two different datasets were trialled for model training. One with ca. 30 images per breed, another with ca. 150 images per breed. The latter performed better, but still required implementation of transfer learning i.e. using a pre-trained base model to produce sufficient results.  |'
    #             '| The model can predict the species of the animal with 95% accuracy | The model will be evaluated on a test set of images to determine its accuracy in predicting the species of the animals. The results will be displayed on a dashboard. | The best accuracy achieved was around 80%. Whilst this failed to meet the 95% target, it was enough to provide the functionality required by the client of providing the top 3 breeds based on probability. |'
    #             '| The model can predict the top 3 animals the image may belong to, in the event that the model is unable to predict the species of the animal with 95% certainty | The model will be evaluated on a test set of images to determine its accuracy in predicting the species of the animals. | The model provides the functionality required by the client of providing the top 3 breeds based on probability. |')

    # st.write

    st.write("### Hypothesis 2 and validation")


# | Hypothesis | Validation | Result |
# | :- | :- | :- |
# |  | The dataset will be reviewed to ensure that it contains a diverse range of animals that the consultants may encounter in practice. | Client was satisfied that the dataset was not deficient in any other animal that was commonly seen during consults. |
# | A Convolutional Neural Network (CNN) can be trained on the dataset of images of animals to accurately predict the animal based on a new and unseen image | The model can accurately predict the breed of an unseen image. | Two different datasets were trialled for model training. One with ca. 30 images per breed, another with ca. 150 images per breed. The latter performed better, but still required implementation of transfer learning i.e. using a pre-trained base model to produce sufficient results.  |
# | The model can predict the species of the animal with 95% accuracy | The model will be evaluated on a test set of images to determine its accuracy in predicting the species of the animals. The results will be displayed on a dashboard. | The best accuracy achieved was around 80%. Whilst this failed to meet the 95% target, it was enough to provide the functionality required by the client of providing the top 3 breeds based on probability. |
# | The model can predict the top 3 animals the image may belong to, in the event that the model is unable to predict the species of the animal with 95% certainty | The model will be evaluated on a test set of images to determine its accuracy in predicting the species of the animals. | The model provides the functionality required by the client of providing the top 3 breeds based on probability. |