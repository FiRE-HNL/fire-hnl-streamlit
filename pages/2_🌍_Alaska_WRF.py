import streamlit as st
import leafmap.foliumap as leafmap
from glob import glob
from pathlib import Path

import folium
from streamlit_folium import folium_static
from localtileserver import TileClient, get_leaflet_tile_layer, examples, get_folium_tile_layer
from ipyleaflet import Map

# First, create a tile server from local raster file
client = examples.get_san_francisco(client_port=8501, debug=True, port=8080)
print(client)
print(client.server.port)

# Create ipyleaflet tile layer from that server
#t = get_leaflet_tile_layer(client)
t = get_folium_tile_layer(client)

m = folium.Map(center=client.center())#, zoom=client.default_zoom)
m.add_child(t)
folium_static(m)