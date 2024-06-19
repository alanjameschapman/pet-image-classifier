import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.page_hypotheses import page_hypotheses
from app_pages.page_identification import page_identification
from app_pages.page_metrics import page_metrics
from app_pages.page_overview import page_overview

# Create an instance of the app
app = MultiPage(app_name="Dog Breed Identification")

# Add app pages here
app.add_page("Project Hypotheses", page_hypotheses)
app.add_page("Breed Identification", page_identification)
app.add_page("Model Metrics", page_metrics)
app.add_page("Project Overview", page_overview)

app.run()
