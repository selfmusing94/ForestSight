import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from streamlit_extras.colored_header import colored_header
from streamlit_extras.card import card

def generate_time_series_data(location):
    """
    Generate time series data for forest cover over time.
    
    Parameters:
    -----------
    location : str
        The name of the location
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame with date and forest cover percentage
    """
    # Define starting points and rate of change based on location
    if location == "Amazon Rainforest":
        start_value = 95.0
        yearly_change = -1.5
        variation = 0.4
    elif location == "Borneo":
        start_value = 90.0
        yearly_change = -2.2
        variation = 0.5
    elif location == "Congo Basin":
        start_value = 92.0
        yearly_change = -1.1
        variation = 0.3
    else:
        start_value = 88.0
        yearly_change = -1.8
        variation = 0.4
    
    # Generate dates and forest cover values
    start_date = datetime(2000, 1, 1)
    dates = []
    forest_cover = []
    urban_expansion = []
    
    for i in range(92):  # Quarterly data for 23 years (2000-2023)
        current_date = start_date + timedelta(days=i*90)
        dates.append(current_date)
        
        # Calculate forest cover with seasonal variation and long-term trend
        years_passed = i / 4
        seasonal_factor = 0.3 * np.sin(i * np.pi / 2)  # Seasonal variation
        random_factor = variation * np.random.randn()  # Random variation
        
        value = start_value + yearly_change * years_passed + seasonal_factor + random_factor
        forest_cover.append(max(0, min(100, value)))  # Ensure value is between 0 and 100
        
        # Calculate urban expansion (inverse of forest loss but not exactly)
        urban_value = 100 - value
        urban_variation = 0.2 * np.random.randn()
        urban_expansion.append(urban_value + urban_variation)
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'forest_cover': forest_cover,
        'urban_expansion': urban_expansion
    })
    
    # Calculate statistics
    stats = {
        'total_loss': start_value - df['forest_cover'].iloc[-1],
        'avg_yearly_loss': abs(yearly_change),
        'current_coverage': df['forest_cover'].iloc[-1],
        'urban_expansion': df['urban_expansion'].iloc[-1] - df['urban_expansion'].iloc[0]
    }
    
    return df, stats

def time_series_analysis():
    """
    Display time series analysis of forest cover changes.
    """
    colored_header(
        label="Time Series Analysis",
        description="Track forest cover changes over time",
        color_name="green-70"
    )
    
    st.write("Explore how forest cover has changed over time in different regions.")
    
    # Get location from session state
    location = st.session_state.selected_location
    
    # Generate or retrieve time series data
    if st.session_state.time_series_data is None or location != st.session_state.selected_location:
        df, stats = generate_time_series_data(location)
        st.session_state.time_series_data = df
        st.session_state.forest_loss_stats = stats
    else:
        df = st.session_state.time_series_data
        stats = st.session_state.forest_loss_stats
    
    # Display statistics in cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        with card(
            title="Total Forest Loss",
            text=f"{stats['total_loss']:.1f}%",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "140px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.1)",
                    "background-color": "#2e7d32",
                },
                "title": {
                    "color": "white"
                },
                "text": {
                    "font-size": "26px",
                    "font-weight": "bold",
                    "color": "white"
                }
            },
        ):
            st.write("Since 2000")
    
    with col2:
        with card(
            title="Yearly Rate of Loss",
            text=f"{stats['avg_yearly_loss']:.2f}%",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "140px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.1)",
                    "background-color": "#ff9800",
                },
                "title": {
                    "color": "white"
                },
                "text": {
                    "font-size": "26px",
                    "font-weight": "bold",
                    "color": "white"
                }
            },
        ):
            st.write("Average per year")
    
    with col3:
        with card(
            title="Current Coverage",
            text=f"{stats['current_coverage']:.1f}%",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "140px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.1)",
                    "background-color": "#1976d2",
                },
                "title": {
                    "color": "white"
                },
                "text": {
                    "font-size": "26px",
                    "font-weight": "bold",
                    "color": "white"
                }
            },
        ):
            st.write("Remaining forest")
    
    with col4:
        with card(
            title="Urban Expansion",
            text=f"{stats['urban_expansion']:.1f}%",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "140px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.1)",
                    "background-color": "#d32f2f",
                },
                "title": {
                    "color": "white"
                },
                "text": {
                    "font-size": "26px",
                    "font-weight": "bold",
                    "color": "white"
                }
            },
        ):
            st.write("Increased urban areas")
    
    st.markdown("---")
    
    # Time range selector
    st.subheader("Select Time Range")
    time_options = ["Last 5 Years", "Last 10 Years", "Last 20 Years", "All Time"]
    selected_time = st.selectbox("Select period", time_options)
    
    # Filter data based on selected time range
    end_date = df['date'].max()
    if selected_time == "Last 5 Years":
        start_date = end_date - timedelta(days=365*5)
        filtered_df = df[df['date'] >= start_date]
    elif selected_time == "Last 10 Years":
        start_date = end_date - timedelta(days=365*10)
        filtered_df = df[df['date'] >= start_date]
    elif selected_time == "Last 20 Years":
        start_date = end_date - timedelta(days=365*20)
        filtered_df = df[df['date'] >= start_date]
    else:
        filtered_df = df
    
    # Create interactive time series chart
    st.subheader("Forest Cover Over Time")
    fig = px.line(
        filtered_df, 
        x='date', 
        y='forest_cover',
        labels={'date': 'Year', 'forest_cover': 'Forest Cover (%)'},
        title=f"Forest Cover Changes in {location}",
        line_shape='spline',
        template="plotly_white" if st.session_state.theme == "light" else "plotly_dark",
    )
    
    fig.update_traces(
        line=dict(color="#2e7d32", width=3),
        mode='lines+markers',
        marker=dict(size=6, color="#2e7d32", line=dict(width=1, color="#ffffff"))
    )
    
    fig.update_layout(
        height=500,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Arial", size=12),
        margin=dict(l=40, r=40, t=60, b=60),
        xaxis=dict(
            tickfont=dict(family="Arial", size=10),
            title_font=dict(family="Arial", size=14, color="#333333"),
            tickangle=-45,
            gridcolor="rgba(230, 230, 230, 0.5)"
        ),
        yaxis=dict(
            tickfont=dict(family="Arial", size=10),
            title_font=dict(family="Arial", size=14, color="#333333"),
            gridcolor="rgba(230, 230, 230, 0.5)"
        ),
        plot_bgcolor="rgba(255, 255, 255, 0.0)",
        paper_bgcolor="rgba(255, 255, 255, 0.0)",
    )
    
    # Add shaded area under line
    fig.add_traces(
        go.Scatter(
            x=filtered_df['date'],
            y=filtered_df['forest_cover'],
            mode='none',
            fill='tozeroy',
            fillcolor='rgba(46, 125, 50, 0.2)',
            showlegend=False
        )
    )
    
    # Add horizontal line for critical threshold
    fig.add_shape(
        type="line",
        x0=filtered_df['date'].min(),
        x1=filtered_df['date'].max(),
        y0=70,  # Critical threshold
        y1=70,
        line=dict(color="red", width=2, dash="dash"),
    )
    
    # Add annotation for threshold
    fig.add_annotation(
        x=filtered_df['date'].max(),
        y=70,
        text="Critical Threshold",
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        arrowsize=1,
        arrowwidth=2,
        ax=-50,
        ay=-30
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Comparison with urban expansion
    st.subheader("Forest Cover vs. Urban Expansion")
    fig2 = go.Figure()
    
    # Add forest cover line
    fig2.add_trace(
        go.Scatter(
            x=filtered_df['date'],
            y=filtered_df['forest_cover'],
            name="Forest Cover",
            line=dict(color="#2e7d32", width=3),
            mode='lines',
        )
    )
    
    # Add urban expansion line
    fig2.add_trace(
        go.Scatter(
            x=filtered_df['date'],
            y=filtered_df['urban_expansion'],
            name="Urban Expansion",
            line=dict(color="#d32f2f", width=3),
            mode='lines',
        )
    )
    
    fig2.update_layout(
        title=f"Forest Cover vs. Urban Expansion in {location}",
        xaxis_title="Year",
        yaxis_title="Percentage (%)",
        height=500,
        template="plotly_white" if st.session_state.theme == "light" else "plotly_dark",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Arial", size=12),
        margin=dict(l=40, r=40, t=60, b=60),
        plot_bgcolor="rgba(255, 255, 255, 0.0)",
        paper_bgcolor="rgba(255, 255, 255, 0.0)",
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Annual rate of change
    st.subheader("Annual Rate of Forest Loss")
    # Calculate annual rate of change
    annual_data = []
    years = sorted(filtered_df['date'].dt.year.unique())
    
    for i in range(len(years)-1):
        year1 = years[i]
        year2 = years[i+1]
        
        # Get average forest cover for each year
        cover1 = filtered_df[filtered_df['date'].dt.year == year1]['forest_cover'].mean()
        cover2 = filtered_df[filtered_df['date'].dt.year == year2]['forest_cover'].mean()
        
        # Calculate rate of change
        rate = cover1 - cover2
        
        annual_data.append({
            'year': year2,
            'rate': rate
        })
    
    if annual_data:
        annual_df = pd.DataFrame(annual_data)
        
        # Create bar chart
        fig3 = px.bar(
            annual_df,
            x='year',
            y='rate',
            labels={'year': 'Year', 'rate': 'Annual Forest Loss (%)'},
            title=f"Annual Rate of Forest Loss in {location}",
            template="plotly_white" if st.session_state.theme == "light" else "plotly_dark",
            color='rate',
            color_continuous_scale=[(0, "#e8f5e9"), (1, "#2e7d32")],
        )
        
        fig3.update_layout(
            height=400,
            coloraxis_showscale=False,
            font=dict(family="Arial", size=12),
            margin=dict(l=40, r=40, t=60, b=60),
            plot_bgcolor="rgba(255, 255, 255, 0.0)",
            paper_bgcolor="rgba(255, 255, 255, 0.0)",
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    
    # Future projection
    st.subheader("Future Projection")
    
    # Add projection years selector
    projection_years = st.slider("Years to project into the future", 1, 20, 10)
    
    # Get the last date and value
    last_date = df['date'].max()
    last_value = df.loc[df['date'] == last_date, 'forest_cover'].values[0]
    
    # Calculate projected values
    projected_dates = [last_date + timedelta(days=365*i) for i in range(1, projection_years+1)]
    
    # Use the average yearly loss rate with some randomness
    yearly_loss = stats['avg_yearly_loss']
    projected_values = []
    current_value = last_value
    
    for _ in range(projection_years):
        # Add some randomness to the yearly loss
        random_factor = 0.2 * np.random.randn()
        adjusted_loss = yearly_loss * (1 + random_factor)
        
        # Calculate new value
        current_value = max(0, current_value - adjusted_loss)
        projected_values.append(current_value)
    
    # Create projection DataFrame
    projection_df = pd.DataFrame({
        'date': projected_dates,
        'forest_cover': projected_values
    })
    
    # Combine historical and projected data
    combined_df = pd.concat([df, projection_df])
    
    # Create the projection chart
    fig4 = go.Figure()
    
    # Add historical data
    fig4.add_trace(
        go.Scatter(
            x=df['date'],
            y=df['forest_cover'],
            name="Historical Data",
            line=dict(color="#2e7d32", width=3),
            mode='lines',
        )
    )
    
    # Add projection
    fig4.add_trace(
        go.Scatter(
            x=projection_df['date'],
            y=projection_df['forest_cover'],
            name="Projected Data",
            line=dict(color="#ff9800", width=3, dash="dot"),
            mode='lines',
        )
    )
    
    # Highlight the current year
    fig4.add_vline(
        x=last_date, 
        line_dash="dash", 
        line_color="rgba(0, 0, 0, 0.5)",
        annotation_text="Current",
        annotation_position="top right"
    )
    
    fig4.update_layout(
        title=f"Forest Cover Projection for {location} (Next {projection_years} Years)",
        xaxis_title="Year",
        yaxis_title="Forest Cover (%)",
        height=500,
        template="plotly_white" if st.session_state.theme == "light" else "plotly_dark",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Arial", size=12),
        margin=dict(l=40, r=40, t=60, b=60),
        plot_bgcolor="rgba(255, 255, 255, 0.0)",
        paper_bgcolor="rgba(255, 255, 255, 0.0)",
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Calculate when forest cover might reach critical levels
    if projected_values:
        critical_threshold = 50  # Define critical threshold
        years_to_critical = None
        
        for i, value in enumerate(projected_values):
            if value <= critical_threshold:
                years_to_critical = i + 1
                break
        
        if years_to_critical:
            st.warning(f"⚠️ At the current rate of deforestation, {location} could reach a critical forest cover of {critical_threshold}% within approximately {years_to_critical} years.")
        else:
            # Calculate how long until critical threshold based on current rate
            years_to_critical = (last_value - critical_threshold) / yearly_loss
            if years_to_critical > 0:
                st.info(f"ℹ️ At the current rate of deforestation, {location} could reach a critical forest cover of {critical_threshold}% in approximately {int(years_to_critical)} years.")
            else:
                st.success(f"✅ {location} is not projected to reach critical forest cover levels within the foreseeable future.")