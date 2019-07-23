import folium
import pandas

data = pandas.read_csv("landmarks.csv")
lat = list(data["Lat"])
lon = list(data["Lon"])
loc_name = list(data["Name"])
park = list(data["Park"])

def colour_picker(park):
    if park == "yes":
        return 'green'
    else:
        return 'red'

map = folium.Map(location=[53.349482, -6.256448], zoom_start=12)

fg = folium.FeatureGroup(name="Dublin Landmarks")

for lt, ln, nm, pk in zip(lat, lon, loc_name, park):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color=colour_picker(pk))))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("map1.html")