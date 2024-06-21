import streamlit as st


# BACKGROUND_IMAGE = 'https://i.imgur.com/Y9PEcSM.png'
ICON = 'https://www.flaticon.com/free-icon/footprint_9707691?term=puppy&page=1&position=4&origin=search&related_id=9707691'


# Define CSS style
# def set_background(image):
#     '''Set background image'''
#     style = f"""
#     <style>
#     .stApp {{
#         background-image: url("{image}");
#         background-size: 18%;
#         background-position: top right;
#         background-repeat: no-repeat;
#     }}
#     </style>
#     """
#     st.markdown(style, unsafe_allow_html=True)


class MultiPage:
    ''' Class to create a multipage app in Streamlit'''

    def __init__(self, app_name) -> None:
        '''Constructor'''
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=ICON)

        # set_background(BACKGROUND_IMAGE)

    def add_page(self, title, func) -> None:
        '''Add a page to the multipage app'''
        self.pages.append({"title": title, "function": func})

    def run(self):
        '''Run the app'''
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
