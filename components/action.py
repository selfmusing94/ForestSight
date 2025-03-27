import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.card import card
import base64
from PIL import Image
from io import BytesIO

def action_section():
    """Display call-to-action section for conservation efforts."""
    colored_header(
        label="Take Action",
        description="Join efforts to protect our forests",
        color_name="green-90"
    )

    st.write("""
    Deforestation is one of the biggest threats to our planet's biodiversity and climate stability. 
    There are many ways you can contribute to forest conservation efforts and help combat deforestation.
    """)
    
    # Create three columns for different action categories
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # First create the card
        card(
            title="Reduce Your Impact",
            text="Simple daily actions to help forests",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "250px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 15px rgba(0,0,0,0.1)",
                    "background-color": "#f1f8e9",
                    "border-left": "4px solid #43a047",
                },
                "title": {
                    "color": "#2e7d32",
                    "font-size": "18px",
                },
            },
        )
        # Then add the content
        st.markdown("""
        • Choose recycled or FSC-certified paper products
        • Reduce meat consumption 
        • Use digital documents instead of printing
        • Support sustainable palm oil products
        • Buy furniture from sustainable sources
        """)
    
    with col2:
        # First create the card
        card(
            title="Support Organizations",
            text="Conservation groups fighting deforestation",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "250px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 15px rgba(0,0,0,0.1)",
                    "background-color": "#e8f5e9",
                    "border-left": "4px solid #2e7d32",
                },
                "title": {
                    "color": "#2e7d32",
                    "font-size": "18px",
                },
            },
        )
        # Then add the content
        st.markdown("""
        • [Rainforest Alliance](https://www.rainforest-alliance.org/)
        • [World Wildlife Fund](https://www.worldwildlife.org/)
        • [Conservation International](https://www.conservation.org/)
        • [The Nature Conservancy](https://www.nature.org/)
        • [Amazon Conservation Team](https://www.amazonteam.org/)
        """)
    
    with col3:
        # First create the card
        card(
            title="Get Involved",
            text="Direct action opportunities",
            image=None,
            styles={
                "card": {
                    "width": "100%",
                    "height": "250px",
                    "border-radius": "10px",
                    "box-shadow": "0 0 15px rgba(0,0,0,0.1)",
                    "background-color": "#dcedc8",
                    "border-left": "4px solid #689f38",
                },
                "title": {
                    "color": "#2e7d32",
                    "font-size": "18px",
                },
            },
        )
        # Then add the content
        st.markdown("""
        • Participate in local tree planting events
        • Volunteer with conservation organizations
        • Support political actions for forest protection
        • Start a community garden
        • Educate others about deforestation
        """)
    
    st.markdown("---")
    
    # Advocacy and education section
    st.subheader("Spread Awareness")
    
    st.write("""
    One of the most effective ways to combat deforestation is by educating others about its impact. 
    Share the knowledge you've gained from this dashboard with friends, family, and colleagues.
    """)
    
    # Educational resources
    with st.expander("Educational Resources"):
        st.markdown("""
        ### Learn More About Deforestation
        
        **Documentaries:**
        - "Our Planet" (Netflix)
        - "A Life on Our Planet" (Netflix)
        - "The Amazon" (National Geographic)
        
        **Books:**
        - "The World's Forests: Ecology and Sustainability" by James Barlow
        - "The Hidden Life of Trees" by Peter Wohlleben
        - "The Sixth Extinction" by Elizabeth Kolbert
        
        **Online Courses:**
        - [Conservation and Protected Area Management](https://www.edx.org/course/conservation-protected-area-management-course-v1queensu-environmental-managementx)
        - [Tropical Forest Landscapes](https://www.edx.org/course/tropical-forest-landscapes)
        """)
    
    # Newsletter signup form (simulated)
    st.subheader("Stay Updated")
    
    with st.form("newsletter_form"):
        st.write("Join our newsletter to receive regular updates on deforestation trends and conservation efforts.")
        
        cols = st.columns([3, 2])
        with cols[0]:
            email = st.text_input("Email Address", placeholder="your.email@example.com")
        
        with cols[1]:
            interests = st.multiselect(
                "Areas of Interest",
                options=["Amazon Rainforest", "Borneo", "Congo Basin", "Other Regions", "Conservation Projects", "Policy Updates"]
            )
        
        submit = st.form_submit_button("Subscribe")
        
        if submit:
            if email and "@" in email and "." in email:
                st.success("Thank you for subscribing! You'll receive our next newsletter soon.")
            else:
                st.error("Please enter a valid email address.")
    
    # Simulated petition
    st.subheader("Sign Our Petition")
    
    st.write("""
    Join thousands of others in calling for stronger protections for the world's forests. 
    Your voice can make a difference in shaping conservation policies.
    """)
    
    petition_count = 8742  # Simulated number of signatures
    
    st.progress(petition_count / 10000)
    st.caption(f"{petition_count:,} people have signed. Goal: 10,000 signatures")
    
    with st.form("petition_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name")
        
        with col2:
            country = st.selectbox(
                "Country",
                options=["United States", "Canada", "United Kingdom", "Australia", "Germany", "France", "Brazil", "India", "Other"]
            )
        
        reason = st.text_area("Why is forest conservation important to you? (Optional)", max_chars=200)
        
        agree = st.checkbox("I agree to have my name displayed publicly as a supporter")
        
        submit_petition = st.form_submit_button("Sign Petition")
        
        if submit_petition:
            if name and agree:
                st.success(f"Thank you, {name}! Your signature has been added.")
                st.balloons()
            else:
                if not name:
                    st.error("Please enter your name.")
                if not agree:
                    st.error("You must agree to have your name displayed publicly.")
    
    # Donation section
    st.subheader("Support Conservation Efforts")
    
    st.write("""
    Your financial contribution can directly support forest conservation projects around the world.
    Below are some organizations accepting donations for deforestation prevention and reforestation efforts.
    """)
    
    orgs = [
        {
            "name": "Rainforest Trust",
            "description": "Purchases and protects the most threatened tropical forests.",
            "link": "https://www.rainforesttrust.org/"
        },
        {
            "name": "One Tree Planted",
            "description": "Plants one tree for every dollar donated.",
            "link": "https://onetreeplanted.org/"
        },
        {
            "name": "Amazon Watch",
            "description": "Protects the rainforest and advances indigenous rights.",
            "link": "https://amazonwatch.org/"
        },
        {
            "name": "Rainforest Foundation",
            "description": "Supports indigenous peoples and traditional populations.",
            "link": "https://rainforestfoundation.org/"
        }
    ]
    
    for i, org in enumerate(orgs):
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                st.write("")  # Placeholder for logo (in a real app, you might display logos)
            
            with col2:
                st.markdown(f"**{org['name']}**")
                st.write(org['description'])
            
            with col3:
                st.markdown(f"[Donate]({org['link']})")
            
        if i < len(orgs) - 1:
            st.markdown("---")