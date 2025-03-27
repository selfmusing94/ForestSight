import streamlit as st
import os
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.card import card
from streamlit_extras.stylable_container import stylable_container

# Import components
from components.header import create_header
from components.upload import upload_section
from components.analysis import analysis_section
from components.timelapse import timelapse_section
from components.statistics import statistics_section
from components.time_series import time_series_analysis
from components.download import download_section
from components.action import action_section
from components.realtime_mapping import realtime_mapping_section

# Set page configuration
st.set_page_config(
    page_title="Deforestation Analysis Dashboard",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS file
def load_css():
    with open('.streamlit/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply CSS styling
load_css()

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
if 'theme' not in st.session_state:
    st.session_state.theme = "light"
if 'time_series_data' not in st.session_state:
    st.session_state.time_series_data = None
if 'forest_loss_stats' not in st.session_state:
    st.session_state.forest_loss_stats = {}

# Function to toggle theme
def toggle_theme():
    if st.session_state.theme == "light":
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"
    
    # Apply theme
    if st.session_state.theme == "dark":
        # Dark theme
        st.markdown("""
        <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
        }
        .css-1d391kg {
            background-color: #262730;
        }
        .st-bq {
            background-color: #262730;
        }
        .css-1oe6wy4 {
            background-color: #1f2229;
        }
        /* Ensure text is visible in dark mode */
        .element-container, .stMarkdown, .stText {
            color: white !important;
        }
        .stTextInput > div > div > input {
            color: white !important;
        }
        .stTextArea > div > div > textarea {
            color: white !important;
        }
        .stNumberInput > div > div > input {
            color: white !important;
        }
        .stSelectbox > div > div > div {
            color: white !important;
        }
        .stMultiselect > div > div > div {
            color: white !important;
        }
        /* Make tables more readable in dark mode */
        .stTable, .dataframe, th, td {
            color: white !important;
            border-color: #4b4b4b !important;
        }
        .dataframe {
            background-color: #1f2229 !important;
        }
        /* Fix DataFrames in dark mode */
        .stDataFrame {
            background-color: #0e1117;
        }
        .stDataFrame [data-testid="stTable"] {
            background-color: #1f2229 !important;
            color: white !important;
        }
        .stDataFrame [data-testid="stTable"] th {
            background-color: #262730 !important;
            color: white !important;
            border-bottom: 1px solid #4b4b4b !important;
        }
        /* Fix sliders and other inputs */
        .stSlider label, .stSlider p {
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        # Light theme (default)
        st.markdown("""
        <style>
        .main {
            background-color: white;
            color: #262730;
        }
        .stApp {
            background-color: white;
        }
        </style>
        """, unsafe_allow_html=True)

# Apply current theme
if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stApp {
        background-color: #0e1117;
    }
    .css-1d391kg {
        background-color: #262730;
    }
    .st-bq {
        background-color: #262730;
    }
    .css-1oe6wy4 {
        background-color: #1f2229;
    }
    /* Ensure text is visible in dark mode */
    .element-container, .stMarkdown, .stText {
        color: white !important;
    }
    .stTextInput > div > div > input {
        color: white !important;
    }
    .stTextArea > div > div > textarea {
        color: white !important;
    }
    .stNumberInput > div > div > input {
        color: white !important;
    }
    .stSelectbox > div > div > div {
        color: white !important;
    }
    .stMultiselect > div > div > div {
        color: white !important;
    }
    /* Make tables more readable in dark mode */
    .stTable, .dataframe, th, td {
        color: white !important;
        border-color: #4b4b4b !important;
    }
    .dataframe {
        background-color: #1f2229 !important;
    }
    /* Fix DataFrames in dark mode */
    .stDataFrame {
        background-color: #0e1117;
    }
    .stDataFrame [data-testid="stTable"] {
        background-color: #1f2229 !important;
        color: white !important;
    }
    .stDataFrame [data-testid="stTable"] th {
        background-color: #262730 !important;
        color: white !important;
        border-bottom: 1px solid #4b4b4b !important;
    }
    /* Fix sliders and other inputs */
    .stSlider label, .stSlider p {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Create header
create_header()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Upload Satellite Image", "Analysis Results", "Time-lapse View", "Real-Time Monitoring", "Statistics & Metrics", 
     "Time-Series Analysis", "Download Reports", "Take Action"]
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
# Theme toggle
st.sidebar.header("Appearance")
theme_toggle = st.sidebar.button(
    "Toggle Dark/Light Mode", 
    on_click=toggle_theme,
    key="theme_toggle",
    help="Switch between dark and light mode"
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
    
elif page == "Real-Time Monitoring":
    realtime_mapping_section()
    
elif page == "Statistics & Metrics":
    statistics_section()
    
elif page == "Time-Series Analysis":
    time_series_analysis()
    
elif page == "Download Reports":
    download_section()
    
elif page == "Take Action":
    action_section()

# Footer
st.markdown("---")
st.markdown("© 2025 Deforestation Analysis Dashboard | Built with Streamlit")
