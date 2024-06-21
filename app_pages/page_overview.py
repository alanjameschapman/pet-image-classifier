import streamlit as st


def page_overview():
    '''Function to display the project overview page'''

    st.header("Project Overview")

    st.write('The client is an online veterinary clinic that offers video '
            'consultations with veterinarians. The client wants to develop an '
            'image classification dashboard that can identify the breed of a dog based '
            'on an image provided by the owner. This will help the '
            'consultants prepare for the consultation and ultimately provide better '
            'care for the dogs.\n\n'
            'The dashboard should also display the top 3 breeds that the '
            'dog might belong to according to model certainty. An intuitive and quantitive '
            'probability of each breed will be '
            'provided to help the consultant determine the animal in-consult. '
            'This will be particularly useful if the dog is mixed breed. ')

    st.write('Click [here](https://github.com/alanjameschapman/pet-image-classifier) to go to the GitHub repository - opens in new tab')