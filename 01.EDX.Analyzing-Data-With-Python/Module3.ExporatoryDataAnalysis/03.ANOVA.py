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
drive_wheels_counts = df["drive-wheels"].value_counts()
drive_wheels_counts.rename(columns={"drive-wheels":"value_counts"}, inplace = True)
drive_wheels_counts.index.name = 'drive-wheels'


df["price"] = df["price"].astype("int")

df_anova = df[["make", "price"]]
grouped_anova = df_anova.groupby(["make"])
anova_results_1 = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("subaru")["price"])
anova_results_2 = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("jaguar")["price"])

# We have a strong correlation between categorical variables, 
# if ANOVA test give us large F value and small p value (<0.05)
print(anova_results_1)
print(anova_results_2)

# df_test = df[["drive-wheels", "body-style", "price"]]
# df_group = df_test.groupby(["drive-wheels", "body-style"], as_index = False)
# df_pivot = df_group.mean().pivot(index = "drive-wheels", columns = "body-style")
# print(df_group.mean())
# print('-------------')
# print(df_pivot)

# #heat map

# plt.pyplot.pcolor(df_pivot, cmap='RdBu')
# plt.pyplot.colorbar()
# plt.pyplot.show()

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df.to_csv("./data/changed-85-dealing-with-missing-values.csv", index=False)

