import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_extras.badges import badge

def create_header():
    """Create the header section of the dashboard with enhanced styling and professional animations."""
    
    # Apply advanced styling to the header with more animations
    st.markdown("""
    <style>
    .header-container {
        display: flex;
        align-items: center;
        padding: 1.5rem;
        border-radius: 12px;
        background: linear-gradient(90deg, rgba(46,125,50,0.2) 0%, rgba(255,255,255,0) 100%);
        margin-bottom: 1.5rem;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        animation: slideDown 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
    }
    
    /* Dark mode header container */
    body.dark .header-container,
    .dark-mode-active .header-container {
        background: linear-gradient(90deg, rgba(46,125,50,0.3) 0%, rgba(30,30,30,0) 100%) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2) !important;
    }
    
    .header-container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #2e7d32, #81c784);
        animation: shimmer 3s infinite linear;
        background-size: 200% 100%;
    }
    
    @keyframes shimmer {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
    
    @keyframes slideDown {
        from {opacity: 0; transform: translateY(-30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    
    @keyframes scaleIn {
        from {transform: scale(0.9); opacity: 0;}
        to {transform: scale(1); opacity: 1;}
    }
    
    .logo-container {
        font-size: 3.8em;
        margin-right: 1.5rem;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
        animation: bounceIn 1.2s cubic-bezier(0.215, 0.61, 0.355, 1);
    }
    
    @keyframes bounceIn {
        0% { transform: scale(0.3); opacity: 0; }
        40% { transform: scale(1.1); }
        80% { transform: scale(0.9); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .text-container h1 {
        margin: 0;
        padding: 0;
        color: #2e7d32;
        font-weight: 800;
        font-size: 2.7rem;
        letter-spacing: -0.5px;
        animation: fadeInRight 0.8s ease-out forwards;
        opacity: 0;
        animation-delay: 0.2s;
    }
    
    /* Dark mode header text */
    body.dark .text-container h1,
    .dark-mode-active .text-container h1 {
        color: #4caf50 !important;
    }
    
    .text-container p {
        margin-top: 0.5rem;
        font-size: 1.1rem;
        opacity: 0;
        line-height: 1.6;
        animation: fadeInRight 0.8s ease-out forwards;
        animation-delay: 0.4s;
        color: #555;
    }
    
    /* Dark mode paragraph text */
    body.dark .text-container p,
    .dark-mode-active .text-container p {
        color: #e0e0e0 !important;
    }
    
    @keyframes fadeInRight {
        from {opacity: 0; transform: translateX(20px);}
        to {opacity: 0.9; transform: translateX(0);}
    }
    
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.6rem;
        animation: fadeInUp 0.8s ease-out forwards;
        opacity: 0;
        animation-delay: 0.6s;
    }
    
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    .badge {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    /* Dark mode badges */
    body.dark .badge,
    .dark-mode-active .badge {
        background-color: rgba(46, 125, 50, 0.2) !important;
        color: #4caf50 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }
    
    .badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: #2e7d32;
        color: white;
    }
    
    /* Dark mode badge hover */
    body.dark .badge:hover,
    .dark-mode-active .badge:hover {
        background-color: #2e7d32 !important;
        color: white !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-between;
        margin: 1.5rem 0;
        animation: fadeIn 1s ease-out forwards;
        animation-delay: 0.8s;
        opacity: 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
        background-color: rgba(46, 125, 50, 0.05);
        transition: all 0.3s ease;
        box-shadow: 0 3px 6px rgba(0,0,0,0.05);
    }
    
    /* Dark mode stat items */
    body.dark .stat-item,
    .dark-mode-active .stat-item {
        background-color: rgba(46, 125, 50, 0.15) !important;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2) !important;
    }
    
    .stat-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    
    .stat-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2e7d32;
        margin: 0;
    }
    
    /* Dark mode stat values */
    body.dark .stat-value,
    .dark-mode-active .stat-value {
        color: #4caf50 !important;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: #555;
        margin: 0;
    }
    
    /* Dark mode stat labels */
    body.dark .stat-label,
    .dark-mode-active .stat-label {
        color: #e0e0e0 !important;
    }
    
    .feature-cards {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .feature-card {
        border-radius: 10px;
        padding: 1rem;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        animation: scaleIn 0.8s ease-out forwards;
        opacity: 0;
    }
    
    /* Dark mode support for feature cards */
    .dark-mode-active .feature-card,
    body.dark .feature-card {
        background-color: #1e1e1e !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    }
    
    .dark-mode-active .feature-card h3,
    body.dark .feature-card h3 {
        color: #4caf50 !important;
    }
    
    .dark-mode-active .feature-card p,
    body.dark .feature-card p {
        color: #e0e0e0 !important;
    }
    
    .feature-card:nth-child(1) {
        animation-delay: 0.9s;
    }
    
    .feature-card:nth-child(2) {
        animation-delay: 1.1s;
    }
    
    .feature-card:nth-child(3) {
        animation-delay: 1.3s;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    .progress-container {
        margin-top: 1rem;
        animation: fadeIn 1s ease-out forwards;
        animation-delay: 1.5s;
        opacity: 0;
    }
    
    .progress-label {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        color: #555;
    }
    
    /* Dark mode progress label */
    body.dark .progress-label,
    .dark-mode-active .progress-label {
        color: #e0e0e0 !important;
    }
    
    .progress-bar {
        height: 8px;
        background-color: #e0e0e0;
        border-radius: 4px;
        overflow: hidden;
    }
    
    /* Dark mode progress bar */
    body.dark .progress-bar,
    .dark-mode-active .progress-bar {
        background-color: #333333 !important;
    }
    
    .progress-value {
        height: 100%;
        background: linear-gradient(90deg, #2e7d32, #81c784);
        border-radius: 4px;
        transition: width 1.5s cubic-bezier(0.19, 1, 0.22, 1);
        width: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create enhanced header with HTML for better styling and animations
    st.markdown("""
    <div class="header-container">
        <div class="logo-container">🌳</div>
        <div class="text-container">
            <h1>Deforestation Analysis Dashboard</h1>
            <p>This interactive dashboard helps visualize and analyze deforestation patterns using satellite imagery and advanced data visualization.</p>
            <div class="badge-container">
                <span class="badge">Interactive Maps</span>
                <span class="badge">Time-Series Analysis</span>
                <span class="badge">Satellite Imagery</span>
                <span class="badge">Real-time Monitoring</span>
                <span class="badge">Conservation Planning</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add global statistics with animations
    st.markdown("""
    <div class="stats-container">
        <div class="stat-item">
            <p class="stat-value">15.3B</p>
            <p class="stat-label">🌲 Trees Cut This Year</p>
        </div>
        <div class="stat-item">
            <p class="stat-value">4.8M</p>
            <p class="stat-label">⏱️ Hectares Lost</p>
        </div>
        <div class="stat-item">
            <p class="stat-value">-2.1%</p>
            <p class="stat-label">📊 Annual Change</p>
        </div>
        <div class="stat-item">
            <p class="stat-value">38.9%</p>
            <p class="stat-label">🌊 Water Impact</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add global conservation goal progress bar with animation
    goal_percentage = 72
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-label">
            <span>Global Forest Conservation Goal</span>
            <span>{goal_percentage}%</span>
        </div>
        <div class="progress-bar">
            <div class="progress-value" style="width: {goal_percentage}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add colored subheader using streamlit-extras
    colored_header(
        label="Monitoring Forest Coverage Worldwide",
        description="Use the sidebar to navigate through different features and analysis tools",
        color_name="green-70"
    )
    
    # Add additional dark mode support styles
    st.markdown("""
    <style>
    .feature-card-title {
        margin: 0; 
        color: #2e7d32; 
        font-size: 1.2rem;
    }
    
    .feature-card-text {
        margin: 0.5rem 0 0 0; 
        font-size: 0.9rem; 
        color: #555;
    }
    
    /* Dark mode styles */
    body.dark .feature-card-title,
    .dark-mode-active .feature-card-title {
        color: #4caf50 !important;
    }
    
    body.dark .feature-card-text,
    .dark-mode-active .feature-card-text {
        color: #e0e0e0 !important;
    }
    
    body.dark .stat-label,
    .dark-mode-active .stat-label {
        color: #e0e0e0 !important;
    }
    
    body.dark .progress-label,
    .dark-mode-active .progress-label {
        color: #e0e0e0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display feature cards with more appealing design and animations
    st.markdown("""
    <div class="feature-cards">
        <div class="feature-card">
            <h3 class="feature-card-title">👁️ Visual Analysis</h3>
            <p class="feature-card-text">Analyze satellite imagery with AI-powered detection algorithms</p>
        </div>
        <div class="feature-card">
            <h3 class="feature-card-title">📊 Statistical Insights</h3>
            <p class="feature-card-text">Comprehensive metrics and trend analysis of deforestation data</p>
        </div>
        <div class="feature-card">
            <h3 class="feature-card-title">🌐 Geographic Mapping</h3>
            <p class="feature-card-text">Interactive maps with real-time deforestation alerts and patterns</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
