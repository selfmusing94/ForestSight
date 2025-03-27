import folium
import random
from folium.plugins import HeatMap
from data.sample_coordinates import get_coordinates_for_location

def create_map_with_deforestation(center_lat, center_lon, zoom, deforested_areas=None):
    """
    Create an interactive map with deforested areas highlighted.
    
    Parameters:
    -----------
    center_lat : float
        Latitude for the center of the map
    center_lon : float
        Longitude for the center of the map
    zoom : int
        Initial zoom level
    deforested_areas : list, optional
        List of dictionaries containing deforested area information
        
    Returns:
    --------
    folium.Map
        An interactive Folium map
    """
    # Create base map
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=zoom,
        tiles="OpenStreetMap"
    )
    
    # Add satellite view option
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Satellite',
        overlay=False
    ).add_to(m)
    
    # Add a simple scale
    folium.plugins.MeasureControl(position='bottomleft', primary_length_unit='kilometers').add_to(m)
    
    # If we have deforested areas, add them to the map
    if deforested_areas:
        # In a real application, these would be actual geo-coordinates
        # Here we're simulating by generating random coordinates around the center
        
        # Create a feature group for deforested areas
        deforested_group = folium.FeatureGroup(name="Deforested Areas")
        
        for i, area in enumerate(deforested_areas):
            # Generate a random offset from the center (in degrees)
            lat_offset = random.uniform(-0.05, 0.05)
            lon_offset = random.uniform(-0.05, 0.05)
            
            # Calculate coordinate
            area_lat = center_lat + lat_offset
            area_lon = center_lon + lon_offset
            
            # Add a marker with popup
            popup_html = f"""
            <div style="width: 200px;">
                <h4>Deforested Area #{i+1}</h4>
                <p><b>Confidence:</b> {area['confidence']:.2f}</p>
                <p><b>Estimated Area:</b> {area['area_km2']} km²</p>
                <p><b>Status:</b> {"Recent" if area['confidence'] > 0.9 else "Ongoing"}</p>
            </div>
            """
            
            folium.Marker(
                [area_lat, area_lon],
                popup=folium.Popup(popup_html, max_width=300),
                icon=folium.Icon(color="red", icon="tree", prefix="fa")
            ).add_to(deforested_group)
            
            # Add a red circle to highlight the area
            folium.Circle(
                [area_lat, area_lon],
                radius=area['area_km2'] * 100,  # Scale for visibility
                color="red",
                fill=True,
                fill_color="red",
                fill_opacity=0.4,
                tooltip=f"Deforested Area: {area['area_km2']} km²"
            ).add_to(deforested_group)
        
        # Add the deforested areas to the map
        deforested_group.add_to(m)
        
        # Generate heatmap data
        heatmap_data = []
        for i in range(20):  # Generate more points for a better heatmap
            for area in deforested_areas:
                # Add multiple points around each deforested area
                lat_offset = random.uniform(-0.03, 0.03)
                lon_offset = random.uniform(-0.03, 0.03)
                area_lat = center_lat + lat_offset
                area_lon = center_lon + lon_offset
                intensity = area['confidence'] * random.uniform(0.5, 1.0)
                heatmap_data.append([area_lat, area_lon, intensity])
        
        # Add heatmap layer
        HeatMap(heatmap_data, name="Deforestation Intensity").add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    return m

def create_timelapse_map(location, years):
    """
    Create a set of maps showing deforestation over time.
    
    Parameters:
    -----------
    location : str
        Name of the location
    years : list
        List of years to create maps for
        
    Returns:
    --------
    list
        List of folium.Map objects, one for each year
    """
    coordinates = get_coordinates_for_location(location)
    maps = []
    
    for year in years:
        m = folium.Map(
            location=[coordinates["lat"], coordinates["lon"]],
            zoom_start=coordinates["zoom"],
            tiles="OpenStreetMap"
        )
        
        # Add satellite view
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Satellite',
            overlay=False
        ).add_to(m)
        
        # Generate random deforested areas based on year
        # The idea is that more recent years have more deforestation
        num_areas = int((year - 2000) / 5) + 1  # More areas in recent years
        
        deforested_group = folium.FeatureGroup(name=f"Deforestation {year}")
        
        for i in range(num_areas):
            # Random coordinates near the center
            lat_offset = random.uniform(-0.05, 0.05)
            lon_offset = random.uniform(-0.05, 0.05)
            area_lat = coordinates["lat"] + lat_offset
            area_lon = coordinates["lon"] + lon_offset
            
            # Random area size (larger in recent years)
            area_size = random.uniform(0.5, 1.0) * (1 + (year - 2000) / 40)
            
            # Add a circle to represent deforested area
            folium.Circle(
                [area_lat, area_lon],
                radius=area_size * 500,  # Scale for visibility
                color="red",
                fill=True,
                fill_color="red",
                fill_opacity=0.4,
                tooltip=f"Deforested in {year}"
            ).add_to(deforested_group)
        
        deforested_group.add_to(m)
        folium.LayerControl().add_to(m)
        
        # Add year label
        title_html = f'''
            <h3 align="center" style="font-size:16px"><b>Deforestation in {year}</b></h3>
        '''
        m.get_root().html.add_child(folium.Element(title_html))
        
        maps.append(m)
    
    return maps
