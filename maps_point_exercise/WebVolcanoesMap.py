import folium
import pandas

map = folium.Map(location=[40.532478, -118.525962], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lat, long, elevation in zip(latitude, longitude, elevation):
    fg.add_child(folium.CircleMarker(location=[lat, long], popup=str(elevation) + "m", radius=6,
                                     fill_color=color_producer(elevation), color = 'grey', fill_opacity=0.7))

map.add_child(fg)
map.save("Volcanoes.html")