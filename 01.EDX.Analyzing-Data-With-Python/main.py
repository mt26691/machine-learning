import pandas as pd

df = pd.read_csv("./data/imports-85.csv", header=None)

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

# drop missing value if value =  None
# df.dropna(subset=["price"], axis=0)
# print(df.head(5))
# print(df.describe(include="all"))
# print(df.columns)

# print(df.dtypes)

# describe specific columns
# print(df[["length", "compression-ratio"]].describe())
# print(df.info)
# print(df["length"])

# How to drop missing values in python?
# use dataframes.dropna()
# http://prntscr.com/oqu52q
# axis=0 drop entire row
# axis=1 drop entire column

# this code does not change the data frame
# df.dropna(subset=["price"], axis=0)

# to modify the dataframe, you have to use inplace = true
df.dropna(subset=["price"], axis=0, inplace=True)


df.to_csv("./data/changed-85.csv", index=True)

