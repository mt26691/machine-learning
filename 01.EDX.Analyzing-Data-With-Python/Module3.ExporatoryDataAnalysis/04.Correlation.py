import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
from scipy import stats

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


# Pandas give us the function dataframe.replace(missing_value, new_value)
# replace "?" value to NaN value
# convert to type float
df["normalized-losses"] = df["normalized-losses"].astype("float")

# for example, we can deal with normalized-losses columns

mean = df["normalized-losses"].mean()

# # Replace NaN value with mean, if we don't set inplace = True, it will not change the dataframe
df["normalized-losses"].replace(np.nan, mean, inplace = True)

avg_stroke=df['stroke'].astype('float').mean(axis=0)
df['stroke'].replace(np.nan, avg_stroke, inplace = True)

avg_horsepower=df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace = True)

# We can see that four doors are the most common type. 
# We can also use the ".idxmax()" method to calculate for us the most common type automatically:
# replace numb of doors by four
df["num-of-doors"].replace(np.nan, "four", inplace=True)

#drop all rows that do not have price data, since price is the thing we want to predict, 
# unknown price means nothing
# we don't need it.
df.dropna(subset=["price"], axis=0, inplace=True)

df['horsepower']=df['horsepower'].astype('float')
df["price"] = df["price"].astype("int")

pearson_coef, p_value = stats.pearsonr(df["horsepower"], df["price"])

print('Correlation coefficient:')
# close to +1: large positive relationship
# close to -1: large negative relationship
# close to 0: no relationship
print(pearson_coef)
print('P-value:')

# < 0.001 strong certainly in result
# < 0.05 moderate certainly in result
# < 0.1 weak certainly in result
# > 0.1 no certainly in result
print(p_value)

df.reset_index(drop=True, inplace=True)

df.to_csv("./data/changed-85-dealing-with-missing-values.csv", index=False)

