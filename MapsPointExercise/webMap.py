import folium
import pandas

map = folium.Map(location=[40.532478, -118.525962], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])

for lat, long in zip(latitude, longitude):
    fg.add_child(folium.Marker(location=[lat, long], popup="Volcanoes!", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")
