import streamlit as st

def create_header():
    """Create the header section of the dashboard."""
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Display a tree emoji as a logo
        st.markdown("<h1 style='font-size: 3em; text-align: center;'>🌳</h1>", unsafe_allow_html=True)
    
    with col2:
        st.title("Deforestation Analysis Dashboard")
        st.markdown(
            """
            This interactive dashboard helps visualize and analyze deforestation patterns using satellite imagery.
            Navigate through the sidebar to access different features.
            """
        )
    
    st.markdown("---")
