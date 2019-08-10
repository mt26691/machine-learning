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

# Simple feature scaling in python
# newData = oldData/maxOfData
print("Max length: " + (str)(df["length"].max()))
df["length"] = df["length"] / df["length"].max()

df.to_csv("./data/changed-85-normalize-data.csv", index=True)

