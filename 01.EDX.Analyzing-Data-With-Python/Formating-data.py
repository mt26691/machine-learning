import pandas as pd
import numpy as np

df = pd.read_csv("./data/changed-85-nan.csv", header=None)

df.columns = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "Engine type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

# To formating data, we can apply calculation to entire columns
# forexample, converting "mpg" to L/100km in pandas

print(df["city-mpg"].describe())
# df["city-mpg"] = 235 / df["city-mpg"]
# df.rename(columns={"city-mpg": "city-L/100km"}, inplace = True)
df.to_csv("./data/changed-85-formating-city-mpg-to-city-lit-per-100-km.csv", index=True)

