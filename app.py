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
    
    /* File uploader */
    .stFileUploader > div > div {
        color: white !important;
    }
    
    .stFileUploader > div > div > span {
        color: #cccccc !important;
    }
    
    /* Fix for file uploader text */
    .stFileUploader p, .stFileUploader span, .stFileUploader label {
        color: white !important;
    }
    
    /* Make sure file uploader instructions are visible */
    .uploadedFileData p, .stFileUploader [data-testid="stFileUploadDropzone"] p,
    [data-testid="stFileUploadDropzone"] span, [data-testid="stFileUploadDropzone"] small {
        color: white !important;
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

# Enhanced Sidebar with better organization
# Navigation section with icon - using header for cleaner look
st.sidebar.title("🧭 Navigation")

# Organized navigation with sections and icons
options = [
    "Upload Satellite Image", 
    "Analysis Results", 
    "Time-lapse View", 
    "Real-Time Monitoring", 
    "Statistics & Metrics", 
    "Time-Series Analysis", 
    "Download Reports", 
    "Take Action"
]

# Create formatted options with icons
formatted_options = [
    "📤 Upload Satellite Image",
    "🔍 Analysis Results",
    "⏱️ Time-lapse View",
    "🔴 Real-Time Monitoring",
    "📊 Statistics & Metrics",
    "📈 Time-Series Analysis",
    "📁 Download Reports",
    "🌱 Take Action"
]

# Create a dictionary to map formatted options back to original options
option_map = {formatted: original for formatted, original in zip(formatted_options, options)}

# Display radio buttons with formatted options
selected_formatted = st.sidebar.radio(
    "Dashboard Sections",
    formatted_options
)

# Map the selected formatted option back to the original option
page = option_map[selected_formatted]

st.sidebar.markdown("---")

# About section with clean styling
st.sidebar.header("🌍 About")
st.sidebar.markdown(
    """
    This dashboard visualizes deforestation using satellite imagery and advanced analytics. 
    
    🔍 Upload your own satellite imagery or explore our sample locations.
    
    📊 Analyze patterns, view statistics, and monitor changes over time.
    """
)

st.sidebar.markdown("---")

# Appearance section
st.sidebar.header("🎨 Appearance")
current_theme = "Dark" if st.session_state.theme == "dark" else "Light"
st.sidebar.markdown(f"**Current theme:** {current_theme}")
theme_toggle = st.sidebar.button(
    f"Switch to {'Light' if current_theme == 'Dark' else 'Dark'} Mode", 
    on_click=toggle_theme,
    key="theme_toggle",
    help="Switch between dark and light mode"
)

st.sidebar.markdown("---")

# Sample locations section with professional styling
st.sidebar.header("🗺️ Sample Locations")
location = st.sidebar.selectbox(
    "Select a region to analyze",
    ["Amazon Rainforest", "Borneo", "Congo Basin", "Custom Upload"]
)

# Style for location info items
location_info_style = "padding-left: 10px; margin: 5px 0; border-left: 2px solid #4caf50;"

# Add detailed information about the selected location
if location == "Amazon Rainforest":
    st.sidebar.markdown("**Amazon Rainforest**: The largest tropical rainforest in the world, spanning 9 countries.")
    st.sidebar.markdown(f"<div style='{location_info_style}'>🌧️ <b>Annual Rainfall</b>: 2,000-3,000 mm</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>🌳 <b>Tree Species</b>: 16,000+</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>🔥 <b>Deforestation Rate</b>: 0.9% annually</div>", unsafe_allow_html=True)
elif location == "Borneo":
    st.sidebar.markdown("**Borneo**: The third-largest island in the world with ancient rainforests.")
    st.sidebar.markdown(f"<div style='{location_info_style}'>🌧️ <b>Annual Rainfall</b>: 2,500-4,000 mm</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>🦧 <b>Endemic Species</b>: 222 mammals</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>🔥 <b>Deforestation Rate</b>: 1.3% annually</div>", unsafe_allow_html=True)
elif location == "Congo Basin":
    st.sidebar.markdown("**Congo Basin**: Africa's largest contiguous forest and the second-largest tropical rainforest globally.")
    st.sidebar.markdown(f"<div style='{location_info_style}'>🌧️ <b>Annual Rainfall</b>: 1,700-2,200 mm</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>🌳 <b>Area</b>: 2 million square kilometers</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>🔥 <b>Deforestation Rate</b>: 0.3% annually</div>", unsafe_allow_html=True)
elif location == "Custom Upload":
    st.sidebar.markdown("**Custom Upload**: Analyze your own satellite imagery.")
    st.sidebar.markdown(f"<div style='{location_info_style}'>📤 Upload satellite imagery in the Upload section</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>⚙️ Our AI will process and analyze your data</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<div style='{location_info_style}'>📊 View detailed deforestation metrics and visualization</div>", unsafe_allow_html=True)

# Add a small note about data sources
st.sidebar.markdown("---")
st.sidebar.markdown("<small>*Data reflects most recent available statistics. Sources include global forest monitoring agencies and satellite data aggregators.</small>", unsafe_allow_html=True)

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
