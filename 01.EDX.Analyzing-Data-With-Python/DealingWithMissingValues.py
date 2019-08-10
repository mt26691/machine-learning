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

# Pandas give us the function dataframe.replace(missing_value, new_value)
# for example, we can deal with normalized-losses columns
print(df[["normalized-losses"]].describe())

mean = df["normalized-losses"].mean()
print(mean)

# Replace NaN value with mean, if we don't set inplace = True, it will not change the dataframe
df["normalized-losses"].replace(np.nan, mean, inplace = True)
# we can replace the missing value of the average entire of the missing value like mean
# 1 Calculate mean of the normalized losses
# mean = df["normalized-losses"].mean()
# print(mean)
df.to_csv("./data/changed-85-dealing-with-missing-values.csv", index=True)

