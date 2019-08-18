import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./data/automobileEDA.csv")

# regression plot
sns.regplot(x='highway-mpg', y='price', data = df)
pyplot.ylim(0,)
pyplot.show()

#residual plot
sns.residplot(df['highway-mpg'], df['price'])
pyplot.show()
