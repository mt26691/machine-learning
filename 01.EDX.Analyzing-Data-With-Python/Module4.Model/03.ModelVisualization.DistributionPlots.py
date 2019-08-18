import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./data/automobileEDA.csv")

# sns.regplot(x = 'highway-mpg', y='price', data = df)
# pyplot.ylim(0,)

# calculate residual plot between highway mpg and price
# in this case, the residual has a curve
# sns.residplot(df['highway-mpg'], df['price'])

lm = LinearRegression()

# define predictor variable and target variable
Z = df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
Y = df["price"]

# use lm.fit to fit the model and then obtain the prediction
lm.fit(Z, Y)
Yhat = lm.predict(Z)


ax1 = sns.distplot(df["price"], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values", ax=ax1)
pyplot.show()
