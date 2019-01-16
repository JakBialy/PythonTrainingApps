import folium
import pandas

map = folium.Map(tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Population map")

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 20000000
                            else 'orange' if 20000000 <= x['properties']['POP2005'] < 40000000 else 'red'}))

map.add_child(fg)
# it is as a one layer - each children is considered as a one layer
map.add_child(folium.LayerControl())
map.save("Country Map.html")