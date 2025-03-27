import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_extras.badges import badge

def create_header():
    """Create the header section of the dashboard with enhanced styling."""
    
    # Apply modern styling to the header
    st.markdown("""
    <style>
    .header-container {
        display: flex;
        align-items: center;
        padding: 1rem;
        border-radius: 10px;
        background: linear-gradient(90deg, rgba(46,125,50,0.2) 0%, rgba(255,255,255,0) 100%);
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        animation: fadeIn 0.8s ease-in-out;
    }
    
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    .logo-container {
        font-size: 3.5em;
        margin-right: 1rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .text-container h1 {
        margin: 0;
        padding: 0;
        color: #2e7d32;
        font-weight: 800;
        font-size: 2.5rem;
    }
    
    .text-container p {
        margin-top: 0.5rem;
        font-size: 1rem;
        opacity: 0.9;
        line-height: 1.5;
    }
    
    .badge-container {
        display: flex;
        gap: 0.5rem;
        margin-top: 0.5rem;
    }
    
    .badge {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create header with HTML for better styling
    st.markdown("""
    <div class="header-container">
        <div class="logo-container">🌳</div>
        <div class="text-container">
            <h1>Deforestation Analysis Dashboard</h1>
            <p>This interactive dashboard helps visualize and analyze deforestation patterns using satellite imagery.</p>
            <div class="badge-container">
                <span class="badge">Interactive Maps</span>
                <span class="badge">Time-Series Analysis</span>
                <span class="badge">Satellite Imagery</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add colored subheader using streamlit-extras
    colored_header(
        label="Monitoring Forest Coverage Worldwide",
        description="Use the sidebar to navigate through different features and analysis tools",
        color_name="green-70"
    )
    
    # Display badges for features
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("👁️ Visual Analysis", icon="ℹ️")
    with col2:
        st.info("📊 Statistical Insights", icon="ℹ️")
    with col3:
        st.info("🌐 Geographic Mapping", icon="ℹ️")
    
    st.markdown("---")
