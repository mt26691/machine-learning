import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot

df = pd.read_csv("./data/changed-85-dealing-with-missing-values.csv")

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

df["price"]=df["price"].astype(float, copy=True)

plt.pyplot.hist(df["price"])
plt.pyplot.xlabel("price")
plt.pyplot.ylabel("count")
plt.pyplot.title("price bins")

plt.pyplot.show()

bins = np.linspace(min(df["price"]), max(df["price"]), 4)
print(bins)
group_names = ["Low", "Medium", "High"]
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)
df.to_csv("./data/changed-85-bining-data.csv", index=True)

