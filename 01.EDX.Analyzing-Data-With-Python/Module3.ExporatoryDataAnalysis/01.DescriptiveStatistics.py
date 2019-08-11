import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot

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
df.replace("?", np.nan, inplace = True)

# print missing data
missing_data = df.isnull()
print(missing_data.head(5))

#count missing columns
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())

# Pandas give us the function dataframe.replace(missing_value, new_value)
# replace "?" value to NaN value
# convert to type float
df["normalized-losses"] = df["normalized-losses"].astype("float")

# for example, we can deal with normalized-losses columns
print(df[["normalized-losses"]].describe())

mean = df["normalized-losses"].mean()
print(mean)

# # Replace NaN value with mean, if we don't set inplace = True, it will not change the dataframe
df["normalized-losses"].replace(np.nan, mean, inplace = True)

avg_stroke=df['stroke'].astype('float').mean(axis=0)
df['stroke'].replace(np.nan, avg_stroke, inplace = True)

avg_horsepower=df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace = True)

# We can see that four doors are the most common type. 
# We can also use the ".idxmax()" method to calculate for us the most common type automatically:
print(df['num-of-doors'].value_counts())
print(df['num-of-doors'].value_counts().idxmax())
# replace numb of doors by four
df["num-of-doors"].replace(np.nan, "four", inplace=True)

#drop all rows that do not have price data, since price is the thing we want to predict, 
# unknown price means nothing
# we don't need it.
df.dropna(subset=["price"], axis=0, inplace=True)
print("drive-wheels values_counts() ---------------------------")
drive_wheels_counts = df["drive-wheels"].value_counts()
drive_wheels_counts.rename(columns={"drive-wheels":"value_counts"}, inplace = True)
drive_wheels_counts.index.name = 'drive-wheels'
print(drive_wheels_counts)


df["price"] = df["price"].astype("int")

print(df["engine-size"].describe())
x = df["engine-size"]
y = df["price"]

plt.pyplot.scatter(x,y)
plt.pyplot.title("Scatter of Engine size and price")
plt.pyplot.xlabel("Engine size")
plt.pyplot.ylabel("Price")

plt.pyplot.show()

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df.to_csv("./data/changed-85-dealing-with-missing-values.csv", index=False)

