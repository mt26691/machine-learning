import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns

df = pd.read_csv("./data/automobileEDA.csv")


print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

print('Correlation between Engine size and price')
# as Engine size goes up, the price goes up, they have positive relationship
print(df[['engine-size', 'price']].corr())
# sns.regplot(x="engine-size", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

print('Correlation between Highway and price')
# as highway mpg gooes up, the price goes down, so they have negative relationship
print(df[['highway-mpg', 'price']].corr())
# sns.regplot(x="highway-mpg", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

print('Correlation between Peak-rmp and price')
print(df[['peak-rpm', 'price']].corr())
# sns.regplot(x="peak-rpm", y="price", data = df)
# plt.pyplot.ylim(0,)
# plt.pyplot.show()

print('Correlation between stroke and price')
print(df[['stroke', 'price']].corr())
# There is a weak correlation between 
# the variable 'stroke' and 'price.' as such regression will not work well. 
sns.regplot(x="stroke", y="price", data = df)
plt.pyplot.ylim(0,)
plt.pyplot.show()
