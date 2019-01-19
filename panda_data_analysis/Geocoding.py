import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()

# example
# coordinates = nom.geocode("3995 23rd St, San Francisco, CA 94114")
# print(coordinates.latitude)
# print(coordinates.longitude)

df = pandas.read_csv("files/supermarkets.csv")
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude)
print(df.Coordinates[0].longitude)