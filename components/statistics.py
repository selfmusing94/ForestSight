import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def statistics_section():
    """Display statistics and metrics about deforestation."""
    
    st.header("Deforestation Statistics & Metrics")
    
    if not st.session_state.analysis_complete:
        st.warning("No analysis data available. Please upload an image or select a sample location first.")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Deforestation by Land Use")
        
        # Generate sample data based on selected location
        if st.session_state.selected_location == "Amazon Rainforest":
            land_use = {
                "Agriculture": 45,
                "Cattle Ranching": 30,
                "Logging": 15,
                "Mining": 5,
                "Infrastructure": 5
            }
        elif st.session_state.selected_location == "Borneo":
            land_use = {
                "Palm Oil Plantations": 55,
                "Logging": 20,
                "Agriculture": 15,
                "Mining": 7,
                "Urban Development": 3
            }
        elif st.session_state.selected_location == "Congo Basin":
            land_use = {
                "Subsistence Farming": 35,
                "Commercial Logging": 30,
                "Fuelwood Collection": 20,
                "Mining": 10,
                "Infrastructure": 5
            }
        else:  # Custom upload
            land_use = {
                "Unknown": 100
            }
        
        # Create pie chart for land use
        land_use_df = pd.DataFrame({
            'Land Use': land_use.keys(),
            'Percentage': land_use.values()
        })
        
        fig = px.pie(
            land_use_df,
            values='Percentage',
            names='Land Use',
            title=f'Deforestation Drivers in {st.session_state.selected_location}',
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Environmental Impact")
        
        # Create metrics for carbon emissions
        if st.session_state.selected_location != "Custom Upload":
            if st.session_state.selected_location == "Amazon Rainforest":
                carbon_emissions = 120
                biodiversity_loss = 85
                soil_erosion = 70
            elif st.session_state.selected_location == "Borneo":
                carbon_emissions = 150
                biodiversity_loss = 90
                soil_erosion = 75
            else:  # Congo Basin
                carbon_emissions = 90
                biodiversity_loss = 65
                soil_erosion = 50
                
            col1a, col1b, col1c = st.columns(3)
            
            with col1a:
                st.metric(
                    "Carbon Emissions",
                    f"{carbon_emissions}M tons",
                    "1.5%"
                )
                
            with col1b:
                st.metric(
                    "Biodiversity Loss",
                    f"{biodiversity_loss} species",
                    "2.3%"
                )
                
            with col1c:
                st.metric(
                    "Soil Erosion",
                    f"{soil_erosion}K hectares",
                    "0.8%"
                )
        else:
            st.info("Environmental impact metrics are only available for sample locations.")
    
    with col2:
        st.subheader("Historical Deforestation Rates")
        
        # Create sample historical data
        if st.session_state.selected_location != "Custom Upload":
            regions = {
                "Amazon Rainforest": {
                    "1990s": 2.5,
                    "2000s": 3.2,
                    "2010s": 2.8,
                    "2020s": 3.6
                },
                "Borneo": {
                    "1990s": 3.8,
                    "2000s": 4.5,
                    "2010s": 4.0,
                    "2020s": 3.7
                },
                "Congo Basin": {
                    "1990s": 1.2,
                    "2000s": 1.5,
                    "2010s": 1.8,
                    "2020s": 2.0
                }
            }
            
            # Create the historical data for the selected location
            decades = list(regions[st.session_state.selected_location].keys())
            rates = list(regions[st.session_state.selected_location].values())
            
            historical_df = pd.DataFrame({
                'Decade': decades,
                'Deforestation Rate (%)': rates
            })
            
            # Create bar chart
            fig = px.bar(
                historical_df,
                x='Decade',
                y='Deforestation Rate (%)',
                title=f'Historical Deforestation Rates in {st.session_state.selected_location}',
                color='Deforestation Rate (%)',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Global Comparison")
            
            # Sample global comparison data
            global_data = {
                "Amazon": 3.6,
                "Borneo": 3.7,
                "Congo Basin": 2.0,
                "Southeast Asia": 3.2,
                "Central America": 2.8
            }
            
            global_df = pd.DataFrame({
                'Region': list(global_data.keys()),
                'Current Deforestation Rate (%)': list(global_data.values())
            })
            
            # Create horizontal bar chart for global comparison
            fig = px.bar(
                global_df,
                y='Region',
                x='Current Deforestation Rate (%)',
                title='Global Deforestation Rate Comparison',
                color='Current Deforestation Rate (%)',
                color_continuous_scale='Reds',
                orientation='h'
            )
            
            # Highlight the current region
            highlight_region = "Amazon" if st.session_state.selected_location == "Amazon Rainforest" else st.session_state.selected_location
            
            fig.update_traces(
                marker=dict(
                    line=dict(
                        color=['rgba(255,255,0,1)' if region == highlight_region else 'rgba(0,0,0,0)' 
                               for region in global_df['Region']],
                        width=3
                    )
                )
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Historical deforestation data is only available for sample locations.")
            
    # Full-width section for conservation efforts
    st.subheader("Conservation Efforts and Recommendations")
    
    if st.session_state.selected_location != "Custom Upload":
        if st.session_state.selected_location == "Amazon Rainforest":
            conservation_efforts = [
                "Strengthening protected area management",
                "Supporting indigenous land rights",
                "Promoting sustainable agriculture practices",
                "Implementing zero-deforestation supply chain commitments"
            ]
            success_story = "Brazil reduced Amazon deforestation by over 80% between 2004 and 2012 through improved monitoring and enforcement."
            
        elif st.session_state.selected_location == "Borneo":
            conservation_efforts = [
                "Developing sustainable palm oil certification",
                "Restoring degraded peatlands",
                "Creating wildlife corridors between forest fragments",
                "Supporting community-based forest management"
            ]
            success_story = "Heart of Borneo initiative has protected over 22 million hectares of forest across Indonesia, Malaysia, and Brunei."
            
        else:  # Congo Basin
            conservation_efforts = [
                "Improving forest governance and transparency",
                "Developing alternative livelihoods for forest-dependent communities",
                "Expanding protected area networks",
                "Addressing illegal logging through certification schemes"
            ]
            success_story = "Central African Forest Initiative (CAFI) has mobilized over $500 million for forest conservation in the region."
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.write("**Recommended Conservation Strategies:**")
            for effort in conservation_efforts:
                st.markdown(f"- {effort}")
                
        with col4:
            st.write("**Success Story:**")
            st.info(success_story)
            
            st.write("**Additional Resources:**")
            st.markdown("- [Global Forest Watch](https://www.globalforestwatch.org/)")
            st.markdown("- [Deforestation Monitoring Tools](https://www.wri.org/)")
            st.markdown("- [Conservation International](https://www.conservation.org/)")
    else:
        st.info("Conservation recommendations are only available for sample locations.")
    
    # Add a timestamp for the statistics
    st.markdown("---")
    st.caption(f"Statistics generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
