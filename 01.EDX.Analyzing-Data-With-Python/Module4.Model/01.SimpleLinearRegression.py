import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./data/automobileEDA.csv")

lm =LinearRegression()

# define predictor variable and target variable
X = df[['highway-mpg']]
Y = df['price']

# use lm.fit to fit the model and then obtain the prediction
lm.fit(X,Y)

Yhat = lm.predict(X)

# the intercept(b0)
print('The intercept is ', lm.intercept_)
print('the slope is ', lm.coef_)

# the relationship between highway mpg and price is
# Pirce = 38423.30 - 821.733*(highway-mpg)

Yhat = lm.predict(X)

print(Yhat)