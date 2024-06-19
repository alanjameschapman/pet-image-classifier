import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from matplotlib.image import imread
# from src.ml.evaluate_clf import load_test_evaluation


def page_metrics():
    '''Function to display the model metrics page'''

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    # Displaying labels distribution on train, validation and test sets
    # labels_distribution = plt.imread(
    #     f"outputs/{version}/labels_distribution.png")
    # st.image(labels_distribution,
    #          caption='Labels Distribution on Train, Validation and Test Sets')
    # st.write(f"From these metrics...
    # st.write("---")

    # st.write("### Model History")
    # col1, col2 = st.beta_columns(2)
    # with col1:
    #     # Displaying model training accuracy
    #     model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    #     st.image(model_acc, caption='Model Training Accuracy')
    # with col2:
    #     # Displaying model training losses
    #     model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
    #     st.image(model_loss, caption='Model Training Losses')


    # st.write("---")

    # st.write("### Generalised Performance on Test Set")

    # # Loading and displaying test set evaluation metrics (loss and accuracy)
    # # evaluation = load_test_evaluation(version)
    # # df_evaluation = pd.DataFrame(evaluation, index=['Loss', 'Accuracy'])
    # # st.dataframe(df_evaluation)

    # st.write('The model has a loss of ... and an accuracy of ...')

    # st.write("---")

    # # Displaying the confusion matrix
    # # confusion_matrix = plt.imread(f"outputs/{version}/confusion_matrix.png")
    # # st.image(confusion_matrix, caption="Confusion Matrix", width=500)

    # st.write('The matrix has four quadrants:')

    # st.write("### Classification Report")

    # # Displaying the classification report
    # # classification_report = plt.imread(
    # #     f"outputs/{version}/classification_report.png")
    # # st.image(classification_report, caption='Classification Report')

    # st.write('The classification report shows...')

    # st.write("---")

    # st.write("### ROC Curve")
