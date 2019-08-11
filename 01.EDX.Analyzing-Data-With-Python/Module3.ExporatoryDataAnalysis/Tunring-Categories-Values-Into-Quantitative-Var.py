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

# Pandas.get_dummies()
dummies_variables = pd.get_dummies(df["fuel-type"])
dummies_variables.rename(
    columns={"gas": "fuel-type-gas", "diesel": "fuel-type-diesel"}, inplace=True
)

df = pd.concat([df, dummies_variables], axis=1)
df.drop("fuel-type", axis=1, inplace=True)

dummies_aspiration_variables = pd.get_dummies(df["aspiration"])

dummies_aspiration_variables.rename(
    columns={"std": "aspiration-std", "turbo": "aspiration-turbo"}, inplace=True
)

print(dummies_aspiration_variables)

df = pd.concat([df, dummies_aspiration_variables], axis=1)
df.drop("aspiration", axis=1, inplace=True)

df.to_csv("./data/changed-85-turning-category-values-into-variables1.csv", index=True)

