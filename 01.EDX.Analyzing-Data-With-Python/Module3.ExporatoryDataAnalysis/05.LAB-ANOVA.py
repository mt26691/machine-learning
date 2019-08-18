import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns
from scipy import stats

df = pd.read_csv("./data/automobileEDA.csv")

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)

print(grouped_test2.head(2))

print(grouped_test2.get_group('4wd')['price'])

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val) 


f_fwd_rwd_val, p_wd_rwd_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])
print( "ANOVA results (FWD, RWD): F=", f_fwd_rwd_val, ", P =", p_wd_rwd_val )


f_4wd_rwd_val, p_4wd_rwd_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])
print( "ANOVA results (4WD, RWD): F=", f_4wd_rwd_val, ", P =", p_4wd_rwd_val )

f_4wd_fwd_val, p_4wd_fwd_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])
print( "ANOVA results (4WD, FWD): F=", f_4wd_fwd_val, ", P =", p_4wd_fwd_val )
