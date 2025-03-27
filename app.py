import streamlit as st
import os
import numpy as np
from datetime import datetime

# Import components
from components.header import create_header
from components.upload import upload_section
from components.analysis import analysis_section
from components.timelapse import timelapse_section
from components.statistics import statistics_section

# Set page configuration
st.set_page_config(
    page_title="Deforestation Analysis Dashboard",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'analyzed_image' not in st.session_state:
    st.session_state.analyzed_image = None
if 'deforested_areas' not in st.session_state:
    st.session_state.deforested_areas = None
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'selected_location' not in st.session_state:
    st.session_state.selected_location = "Amazon Rainforest"
if 'timelapse_images' not in st.session_state:
    st.session_state.timelapse_images = {}

# Create header
create_header()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Upload Satellite Image", "Analysis Results", "Time-lapse View", "Statistics & Metrics"]
)

st.sidebar.markdown("---")
st.sidebar.header("About")
st.sidebar.info(
    """
    This dashboard visualizes deforestation using satellite imagery. 
    Upload an image or select a sample location to analyze deforestation patterns.
    """
)

st.sidebar.markdown("---")
st.sidebar.header("Sample Locations")
location = st.sidebar.selectbox(
    "Select a region",
    ["Amazon Rainforest", "Borneo", "Congo Basin", "Custom Upload"]
)

if location != st.session_state.selected_location:
    st.session_state.selected_location = location
    st.session_state.analysis_complete = False
    if location != "Custom Upload":
        # This would load predetermined data for the selected location
        st.session_state.analysis_complete = True
    st.rerun()

# Main content based on selected page
if page == "Upload Satellite Image":
    upload_section()
    
elif page == "Analysis Results":
    analysis_section()
    
elif page == "Time-lapse View":
    timelapse_section()
    
elif page == "Statistics & Metrics":
    statistics_section()

# Footer
st.markdown("---")
st.markdown("© 2023 Deforestation Analysis Dashboard | Built with Streamlit")
