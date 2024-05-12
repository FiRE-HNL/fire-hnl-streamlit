import streamlit as st
import leafmap.foliumap as leafmap
from glob import glob
from pathlib import Path

st.set_page_config(layout="wide")

markdown = """
FiRE-HNL Beta Dashboard
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Lightning Forecast (10 days)")

# define layers dict
layers_dict = glob('/Users/jacaraba/Desktop/FiRE-HNL/all_rf_v3_2012-2022_oversampled_2/test-window/*-clipped.tif')

col1, col2 = st.columns([4, 1])
options = layers_dict#list(leafmap.basemaps.keys())
#print(options)
index = 0 #options.index("OpenTopoMap")

with col2:
    current_forecast_date = st.selectbox("Current Forecast Window:", options, index)
    previous_forecast_date = st.selectbox("Previous Forecast Window:", options, index)
    wrf_variable = st.selectbox("WRF Variable:", options, index)

m = leafmap.Map(
    locate_control=True, latlon_control=True,
    draw_export=True, minimap_control=True,
    center=[30, -40],
    zoom=13

)
m.add_basemap("OpenTopoMap")

with col1:

    m.add_raster(
        current_forecast_date,
        bands=[1],
        vmin=0,
        vmax=100,
        colormap='jet',
        layer_name=Path(current_forecast_date).stem
    )
        
    # folium does not support this
    # m.add_time_slider(layers_dict, time_interval=1)
    m.to_streamlit(height=700)
