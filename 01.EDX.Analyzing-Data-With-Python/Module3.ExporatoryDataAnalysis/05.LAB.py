import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns

df = pd.read_csv("./data/automobileEDA.csv")


print(df[["bore", "stroke", "compression-ratio", "horsepower"]].corr())

print("Correlation between Engine size and price")
# as Engine size goes up, the price goes up, they have positive relationship
print(df[["engine-size", "price"]].corr())
# sns.regplot(x="engine-size", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

print("Correlation between Highway and price")
# as highway mpg gooes up, the price goes down, so they have negative relationship
print(df[["highway-mpg", "price"]].corr())
# sns.regplot(x="highway-mpg", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

print("Correlation between Peak-rmp and price")
print(df[["peak-rpm", "price"]].corr())
# sns.regplot(x="peak-rpm", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

print("Correlation between stroke and price")
print(df[["stroke", "price"]].corr())
# There is a weak correlation between
# the variable 'stroke' and 'price.' as such regression will not work well.
# sns.regplot(x="stroke", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

# sns.boxplot(x='body-style', y='price', data = df)

# Here we see that the distribution of price between these two engine-location categories,
# front and rear, are distinct enough to take engine-location as a
# potential good predictor of price.
# sns.boxplot(x='engine-location', y='price', data = df)
# sns.boxplot(x='drive-wheels', y='price', data = df)

# plt.pyplot.show()

# Value-counts is a good way of understanding how many units of each characteristic/variable we have.
# We can apply the "value_counts" method on the column 'drive-wheels'. Don’t forget the method
# "value_counts" only works on Pandas series, not Pandas Dataframes.
# As a result, we only include one bracket "df['drive-wheels']" not two brackets "df[['drive-wheels']]".
drive_wheels_counts = df["drive-wheels"].value_counts().to_frame()
drive_wheels_counts.rename(columns={"drive-wheels": "value_counts"}, inplace=True)
drive_wheels_counts.index.name = "drive-wheels"

print(df["drive-wheels"].value_counts())
print(df["drive-wheels"].unique())

df_group_one = df[["drive-wheels", "body-style", "price"]]
df_group_one = df_group_one.groupby(["drive-wheels", 'body-style'], as_index=False).mean()

print(df_group_one)

df_pivot = df_group_one.pivot(index="drive-wheels", columns="body-style")

# im = plt.pyplot.pcolor(df_pivot, cmap='RdBu')
# plt.pyplot.colorbar()
# plt.pyplot.show()


fig, ax = plt.pyplot.subplots()
im = ax.pcolor(df_pivot, cmap='RdBu')

#label names
row_labels = df_pivot.columns.levels[1]
col_labels = df_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(df_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.pyplot.xticks(rotation=90)

plt.pyplot.colorbar(im)
plt.pyplot.show()

print(df_pivot)

group_body_style = df[["body-style", "price"]]
group_body_style = group_body_style.groupby(['body-style'], as_index = False).mean()
print(group_body_style)