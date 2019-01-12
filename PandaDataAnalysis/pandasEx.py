import pandas

# import examples
# df1 = pandas.read_csv("files/supermarkets.csv")
#
# df2 = pandas.read_json("files/supermarkets.json")
#
# df3 = pandas.read_excel("files/supermarkets.xlsx", sheet_name=0)
#
# df4 = pandas.read_csv("files/supermarkets-commas.txt")
#
# df5 = pandas.read_csv("files/supermarkets-semi-colons.txt", sep=";")
#
# df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
#
# df7 = pandas.read_json("http://pythonhow.com/supermarkets.json")


df = pandas.read_json("files/supermarkets.json")
df = df.set_index("Address")

# slicing
# df = df.loc["735 Dolores St":"332 Hill St", "Country":"ID"]
# df = list(df.loc[:, "Country"])
# df = df.iloc[1:4, 1:4]
# df = df.ix[3, ["Name", "Country"]]

# deleting
# df = df.drop("735 Dolores St", 0)
# df = df.drop(df.columns[0:3], 1)

# updating and adding

# df["Continent"] = df.shape[0] * ["North America"]
# df["Continent"] = df["Country"] + "," + "North America"
# df = df.T
# df["My Address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
# df = df.T


print(df)


