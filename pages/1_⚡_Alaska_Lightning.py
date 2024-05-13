import os
import leafmap as leafmap_api
import streamlit as st
import leafmap.foliumap as leafmap
from glob import glob
from pathlib import Path
from datetime import date, timedelta
from huggingface_hub import hf_hub_download, snapshot_download
import folium

st.set_page_config(layout="wide")

markdown = """
FiRE-HNL Beta Dashboard
Validation of lightning probability maps during fire season 2024.
"""


st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

dataset_path_2016 = snapshot_download(
    repo_id="loboda-umd/fire-hnl-lightning-2016",
    #subfolder="2016-06-01_2016-06-11",
    repo_type="dataset",
    #filename='d02_2016-06-01_00-00-00_0-warp-lightning-clipped.tif'
    #allow_patterns=["*.tif"]
)

dataset_path_2024 = snapshot_download(
    repo_id="loboda-umd/fire-hnl-lightning-2024",
    #subfolder="2016-06-01_2016-06-11",
    repo_type="dataset",
    #filename='d02_2016-06-01_00-00-00_0-warp-lightning-clipped.tif'
    #allow_patterns=["*.tif"]
)

def format_filename(filename):
    return f'{Path(filename).stem}'.split('_')[1]

# define layers dict
options_2024 = [
    'https://data.kitware.com/api/v1/file/626854a14acac99f42126a74/download'
]#sorted(glob(os.path.join(dataset_path_2024, '*/*.tif')))
options_2016 = [
    'https://data.kitware.com/api/v1/file/626854a14acac99f42126a74/download'
]#sorted(glob(os.path.join(dataset_path_2016, '*/*.tif')))

#st.title(f"Lightning Forecast: {format_filename(options_2024[0])} to {format_filename(options_2024[-1])}")
st.title(f"Lightning Forecast")
col1, col2 = st.columns([4, 1])

# options = layers_dict #list(leafmap.basemaps.keys())
# print(options)
index = 0 #options.index("OpenTopoMap")

with col2:
    current_forecast_date = st.selectbox("Current Forecast Window:", options_2024, index)#, format_func=format_filename)
    previous_forecast_date = st.selectbox("Previous Forecast Window:", options_2024, index)#, format_func=format_filename)
    legacy_forecast_date = st.selectbox("Legacy Examples:", options_2016, index)#, format_func=format_filename)

m = leafmap.Map(
    locate_control=True, latlon_control=True,
    draw_export=True, minimap_control=True,
    center=[30, -40],
    zoom=13,
    google_map='terrain'

)
m.add_basemap("OpenTopoMap")

with col1:

    #dataset_path = snapshot_download(
    #    repo_id="loboda-umd/fire-hnl-lightning-2016",
    #    #subfolder="2016-06-01_2016-06-11",
    #    repo_type="dataset",
    #    #filename='d02_2016-06-01_00-00-00_0-warp-lightning-clipped.tif'
    #    #allow_patterns=["*.tif"]
    #)
    print(current_forecast_date)
    m.add_raster(
        current_forecast_date,
        bands=[1],
        vmin=0,
        vmax=100,
        colormap='jet',
        layer_name=Path(current_forecast_date).stem,
        client_port=8501
    )

    # folium does not support this
    # m.add_time_slider(layers_dict, time_interval=1)
    m.to_streamlit(height=700, bidirectional=True)
