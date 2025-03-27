import streamlit as st
import folium
from streamlit_folium import folium_static
import numpy as np
from datetime import datetime
import pandas as pd

from utils.mapping import create_map_with_deforestation
from utils.visualization import create_deforestation_heatmap
from data.sample_coordinates import get_coordinates_for_location

def analysis_section():
    """Display analysis results for deforestation detection."""
    
    st.header("Deforestation Analysis Results")
    
    if not st.session_state.analysis_complete:
        st.warning("No analysis data available. Please upload an image or select a sample location first.")
        return
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("Satellite Imagery with Detected Deforestation")
        
        # Toggle to switch between original and analyzed image
        view_option = st.radio(
            "View:",
            ["Original Image", "Analyzed Image with Deforestation Highlighted"]
        )
        
        if view_option == "Original Image" and st.session_state.uploaded_image is not None:
            st.image(
                st.session_state.uploaded_image, 
                use_container_width=True, 
                caption="Original Satellite Image"
            )
        elif view_option == "Analyzed Image with Deforestation Highlighted" and st.session_state.analyzed_image is not None:
            st.image(
                st.session_state.analyzed_image, 
                use_container_width=True, 
                caption="Deforested Areas Highlighted"
            )
        
        st.subheader("Interactive Map View")
        coordinates = get_coordinates_for_location(st.session_state.selected_location)
        
        map_view = create_map_with_deforestation(
            center_lat=coordinates["lat"],
            center_lon=coordinates["lon"],
            zoom=coordinates["zoom"],
            deforested_areas=st.session_state.deforested_areas
        )
        
        folium_static(map_view)
        
    with col2:
        st.subheader("Analysis Summary")
        
        # Create some sample metrics for the analysis
        if st.session_state.selected_location != "Custom Upload":
            if st.session_state.selected_location == "Amazon Rainforest":
                region = "Amazon Basin"
                country = "Brazil"
                total_area = "5.5 million km²"
                deforested = "17%"
                rate = "0.5%"
            elif st.session_state.selected_location == "Borneo":
                region = "Borneo Island"
                country = "Indonesia/Malaysia"
                total_area = "743,330 km²"
                deforested = "25%"
                rate = "1.3%"
            else:  # Congo Basin
                region = "Congo Basin"
                country = "Democratic Republic of Congo"
                total_area = "3.7 million km²"
                deforested = "10%"
                rate = "0.3%"
        else:
            region = "Custom Region"
            country = "Unknown"
            total_area = "Unknown"
            deforested = "Unknown"
            rate = "Unknown"
        
        metrics_data = {
            "Metric": ["Region", "Country", "Total Forest Area", "Deforested Area", "Annual Deforestation Rate"],
            "Value": [region, country, total_area, deforested, rate]
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        st.table(metrics_df)
        
        st.subheader("Deforestation Heatmap")
        heatmap_fig = create_deforestation_heatmap(st.session_state.selected_location)
        st.plotly_chart(heatmap_fig, use_container_width=True)
        
        st.subheader("Risk Assessment")
        
        # Sample risk assessment based on location
        if st.session_state.selected_location == "Amazon Rainforest":
            risk_level = "High"
            risk_color = "red"
            risk_factors = [
                "Illegal logging operations",
                "Agricultural expansion",
                "Mining activities",
                "Road construction"
            ]
        elif st.session_state.selected_location == "Borneo":
            risk_level = "Very High"
            risk_color = "darkred"
            risk_factors = [
                "Palm oil plantations",
                "Timber extraction",
                "Forest fires",
                "Urban development"
            ]
        elif st.session_state.selected_location == "Congo Basin":
            risk_level = "Medium"
            risk_color = "orange"
            risk_factors = [
                "Subsistence agriculture",
                "Commercial logging",
                "Infrastructure development",
                "Charcoal production"
            ]
        else:
            risk_level = "Unknown"
            risk_color = "gray"
            risk_factors = ["Custom upload - risk factors unknown"]
        
        st.markdown(f"**Risk Level: <span style='color:{risk_color}'>{risk_level}</span>**", unsafe_allow_html=True)
        
        st.write("Contributing factors:")
        for factor in risk_factors:
            st.markdown(f"- {factor}")
            
        # Add a timestamp for the analysis
        st.markdown("---")
        st.caption(f"Analysis timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
