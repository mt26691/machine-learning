import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns
from scipy import stats

df = pd.read_csv("./data/automobileEDA.csv")


print(df[['wheel-base', 'price']].corr())

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

pearson_horse_power_coef, p_horse_power_value = stats.pearsonr(df['horsepower'], df['price'])

# conclusion
# the linear relationship (Pearson correlation) is quite strong (0.8095) that is close to +1
# the p value is very small (< 0.001), so we have a strong, certainly in the result
print("The Pearson Correlation Coefficient between horsepower and price is", pearson_horse_power_coef, " with a P-value of P =", p_horse_power_value)

pearson_length_coef, p_length_value = stats.pearsonr(df['length'], df['price'])
# conclusion
# the linear relationsip is 0.69, so we may have linear here,
# the P value is <0.001 so the correlation between length and price is statistically significant.
print("The Pearson Correlation Coefficient (length and price) is", pearson_length_coef, " with a P-value of P = ", p_length_value)  

pearson_width_coef, p_width_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient (width and price) is", pearson_width_coef, " with a P-value of P = ", p_width_value)  


pearson_curb_weight_coef, p_curb_weight_value = stats.pearsonr(df['curb-weight'], df['price'])
print("The Pearson Correlation Coefficient (curb-weight and price) is", pearson_curb_weight_coef, " with a P-value of P = ", p_curb_weight_value)  
