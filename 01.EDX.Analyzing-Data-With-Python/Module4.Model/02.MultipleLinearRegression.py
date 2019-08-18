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
Z = df[['horsepower', 'curb-weight', 'engine-size','highway-mpg']]
Y = df['price']

# use lm.fit to fit the model and then obtain the prediction
lm.fit(Z ,Y)


# # the intercept(b0)
print('The intercept is ', lm.intercept_)
print('the slope is ', lm.coef_)

Yhat = lm.predict(Z)

print(Yhat)