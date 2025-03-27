import streamlit as st
import io
from PIL import Image
import numpy as np
import datetime
from utils.image_processing import process_satellite_image
from utils.mapping import create_map_with_deforestation

def upload_section():
    """Create the upload section for satellite images."""
    
    st.header("Upload Satellite Imagery")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write(
            """
            Upload satellite imagery to analyze deforestation patterns. 
            The system will process the image and highlight areas where deforestation has been detected.
            
            **Supported formats:** .jpg, .jpeg, .png
            **Recommended resolution:** 1000x1000 pixels or higher
            """
        )
        
        upload_method = st.radio(
            "Select upload method:",
            ["Upload your own image", "Use sample imagery"]
        )
        
        if upload_method == "Upload your own image":
            uploaded_file = st.file_uploader(
                "Choose a satellite image",
                type=["jpg", "jpeg", "png"]
            )
            
            if uploaded_file is not None:
                try:
                    # Read and process the uploaded image
                    image = Image.open(uploaded_file)
                    st.session_state.uploaded_image = image
                    
                    # Process the image (detect deforestation)
                    with st.spinner("Analyzing image for deforestation..."):
                        analyzed_img, deforested_areas = process_satellite_image(image)
                        st.session_state.analyzed_image = analyzed_img
                        st.session_state.deforested_areas = deforested_areas
                        st.session_state.analysis_complete = True
                    
                    st.success("Image analysis complete! Go to Analysis Results to view details.")
                    
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")
        else:
            sample_options = ["Amazon Rainforest (2020)", "Borneo (2021)", "Congo Basin (2019)"]
            sample_selection = st.selectbox("Select a sample image", sample_options)
            
            if st.button("Use this sample"):
                with st.spinner("Loading sample data..."):
                    # In a real application, this would load actual sample data
                    # Here we're simulating the loading of sample data
                    # Generate a sample image for demonstration
                    width, height = 800, 600
                    image_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
                    # Add some green areas to simulate forest
                    image_array[:, :, 1] = np.clip(image_array[:, :, 1] + 100, 0, 255)
                    sample_image = Image.fromarray(image_array)
                    
                    st.session_state.uploaded_image = sample_image
                    analyzed_img, deforested_areas = process_satellite_image(sample_image)
                    st.session_state.analyzed_image = analyzed_img
                    st.session_state.deforested_areas = deforested_areas
                    st.session_state.analysis_complete = True
                    
                    # Generate some timelapse images for the sample
                    years = [2016, 2017, 2018, 2019, 2020]
                    st.session_state.timelapse_images = {}
                    for year in years:
                        # Simulate different images for each year
                        year_array = np.copy(image_array)
                        # Decrease green channel over time to simulate deforestation
                        reduction = (2021 - year) * 15
                        year_array[:, :, 1] = np.clip(year_array[:, :, 1] - reduction, 0, 255)
                        year_image = Image.fromarray(year_array)
                        st.session_state.timelapse_images[year] = year_image
                    
                st.success("Sample data loaded! Navigate to Analysis Results to view details.")
    
    with col2:
        st.subheader("Image Preview")
        if st.session_state.uploaded_image is not None:
            st.image(st.session_state.uploaded_image, use_column_width=True, caption="Uploaded Image")
        else:
            st.info("No image uploaded yet. Please upload an image or select a sample.")
            
            # Show a placeholder for the image preview
            st.markdown(
                """
                <div style="display: flex; justify-content: center; align-items: center; 
                height: 200px; border: 2px dashed #ccc; border-radius: 5px;">
                    <p style="color: #888;">Image preview will appear here</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
