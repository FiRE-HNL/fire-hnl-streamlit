import re
import streamlit as st
import rioxarray as rxr
# import cartopy.crs as ccrs

import matplotlib.pyplot as plt
import streamlit.components.v1 as components

from PIL import Image
from matplotlib.animation import FuncAnimation
# from huggingface_hub import hf_hub_download
# from streamlit_extras.badges import badge

st.set_page_config(
    page_title="Home",
    page_icon="🔥",
)

st.write("# FiRE-HNL Beta Dashboard")

st.sidebar.success("Select a page above.")

st.markdown(
    f"""
    This space was created to test several operational products
    developed for Alaska fire occurrence modeling efforts.
    Select a page from the sidebar to test some of the example
    workflows developed as part of this research.
    
    ## Objectives
    Visualization and download of Alaska fire data. This dashboard
    was tested during the 2023 fire season, and is being improved
    for the 2024 fire season. Updates to the maps are done at 6 AM
    local Alaska time.

    ## Health Status
    - WRF: Normal
    - Lightning: Normal
    - Ignition: In Development
    
    ## Study Area
    """
)

# set study area image in the dashboard
img = Image.open('images/study_area.jpeg')
st.image('https://files.blogs.illinois.edu/files/6367/265408/76088.jpg')#img)

st.markdown(
    """
    Figure 1. Study area.
    """
)

st.markdown(
    """    
    ## Feedback
    We are seeking daily feedback on forecast potential. Feel free
    to reach out directly if you have any feedback or if you have
    additional features that would be useful to improve the information
    provided here.
    
    Curator Email: jacaraba@umd.edu
    """
)