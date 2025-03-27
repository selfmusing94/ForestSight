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
# Initialize theme state
if 'theme' not in st.session_state:
    st.session_state.theme = "light"
if 'timelapse_images' not in st.session_state:
    st.session_state.timelapse_images = {}
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
    # Force rerun to apply theme changes immediately
    st.rerun()  # Use the rerun method to refresh the app

# Apply current theme with dark mode class
if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], 
    [data-testid="stHeader"], [data-testid="stToolbar"], 
    [data-testid="stSidebar"], [data-testid="stMarkdown"] {
        color-scheme: dark;
    }
    
    /* Apply dark class to everything */
    body {
        class: dark;
    }
    
    .dark-mode-active {
        display: block;
    }
    
    /* Primary backgrounds */
    body, .main, .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0e1117 !important;
        color: white !important;
    }
    
    /* Sidebar specific styling */
    [data-testid="stSidebar"] {
        background-color: #1e1e1e !important;
        border-right: 1px solid #333333 !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] [data-testid="stMarkdown"],
    [data-testid="stSidebar"] [role="radiogroup"] label span p {
        color: white !important;
    }
    
    /* Navigation and radio buttons */
    [role="radiogroup"] label {
        color: white !important;
    }
    
    [role="radiogroup"] svg {
        color: white !important;
    }
    
    /* All text elements */
    h1, h2, h3, h4, h5, h6, p, span, label, .element-container,
    .stMarkdown, .stText, [data-testid="stWidgetLabel"] {
        color: white !important;
    }
    
    /* Form inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input {
        color: white !important;
        background-color: #1f2229 !important;
        border-color: #4b4b4b !important;
    }
    
    /* Selectboxes and dropdowns */
    .stSelectbox > div > div > div,
    .stMultiselect > div > div > div {
        color: white !important;
        background-color: #1f2229 !important;
        border-color: #4b4b4b !important;
    }
    
    /* Tables and dataframes */
    .stTable, .dataframe, th, td {
        color: white !important;
        border-color: #4b4b4b !important;
    }
    
    .dataframe {
        background-color: #1f2229 !important;
    }
    
    .stDataFrame {
        background-color: #0e1117 !important;
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
    
    /* Buttons and sliders */
    .stButton button {
        background-color: #4caf50 !important; 
        color: white !important;
        font-weight: 500 !important;
        text-shadow: 0px 0px 1px rgba(0,0,0,0.3) !important;
    }
    
    .stButton button:hover {
        background-color: #45a049 !important;
        border-color: #555 !important;
    }
    
    /* Ensure all button text is visible */
    button, .stButton > button, div[data-testid="stForm"] button {
        color: white !important;
        background-color: #4caf50 !important;
        font-weight: 500 !important;
        text-shadow: 0px 0px 1px rgba(0,0,0,0.3) !important;
    }
    
    /* Radio buttons */
    .stRadio label, .stRadio div, .stRadio p {
        color: white !important;
    }
    
    /* All sliders */
    .stSlider label, .stSlider p, .stSlider div {
        color: white !important;
    }
    
    /* Info boxes */
    [data-testid="stInfo"] {
        background-color: rgba(30, 30, 30, 0.7) !important;
        color: white !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader, .streamlit-expanderContent {
        background-color: #1e1e1e !important;
        color: white !important;
    }
    
    /* All card elements */
    [data-testid="stCard"], .element-container div div div div [data-testid="stHorizontalBlock"] div div {
        background-color: #1e1e1e !important;
        color: white !important;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    /* Feature cards specific */
    .feature-card, .feature-card * {
        color: white !important;
    }
    
    .feature-card-title {
        color: #4caf50 !important;
        font-weight: bold !important;
    }
    
    /* Small text and captions */
    small, .stCaption, caption {
        color: #cccccc !important;
    }
    
    /* Links */
    a:not([style]) {
        color: #4caf50 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Add a class for CSS targeting
    st.markdown('<div class="dark-mode-active" style="display:none"></div>', unsafe_allow_html=True)
else:
    # Light theme - clean slate
    st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        color-scheme: light;
    }
    body {
        color: #262730;
        background-color: white;
    }
    .stApp {
        background-color: white;
    }
    .dark-mode-active {
        display: none;
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
