import streamlit as st
# import matplotlib.pyplot as plt
# from PIL import Image


# image = Image.open("readme_assets/overview.jpg")


def page_overview():
    '''Function to display the project overview page'''

    st.write("### Project Overview")

    st.info('The client is an online veterinary clinic that offers video '
            'consultations with veterinarians. The client wants to develop an '
            'image classifier that can predict the species of an animal based '
            'on an image provided by the animal owner. This will help the '
            'consultants to prepare for the consultation and provide better '
            'care to the animals.\n\n'
            'The dashboard should also display the top 3 species that the '
            'animal may belong to, along with images, in the event that the '
            'model is unable to predict the species of the animal with '
            '95% certainty. The probability of each species will be provided '
            'alongside, to help the consultant determine the animal in-consult.')


    # # st.image(image, 
    # #          caption="Powdery Mildew Detection predicts on cherry leaves images",
    # #          use_column_width=True)

    # st.write('* For additional information...')
