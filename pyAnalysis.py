
# IMPORT LIBRARIES

import pandas as pd
import numpy as np



# INSTALL SEABORN ON JUPYTER

%%capture
! pip install seaborn



# IMPORT VISUALIZATION PACKAGE

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline              # to plot in a Jupyter notebook



# CATEGORICAL DATA

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels':'value_counts'}, inplace = True)
print(drive_wheels_counts)



# BOX PLOTS

sns.boxplot(x='drive-wheels', y='price', data=df)



# SCATTER PLOT

y= df['price']
x= df['engine-size']
plt.scatter(x,y)

plt.title('Scatterplot of Engine Size vs Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')



# GROUP BY

df['drive-wheels'].unique() # group the variable "drive-wheels" by categories

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)


# Let's see if different types 'drive-wheels' impact 'price', we group the data.

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)


# We can obtain the values of the method group using the method "get_group".

grouped_test2.get_group('4wd')['price']


# Pivot table

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot

grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot


# Heatmap

plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


# The default labels convey no useful information to us. Let's change that:

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()



# CORRELATION

df.corr()           # calculate the correlation between variables of type "int64" or "float64"

df[["engine-size", "price"]].corr()     # Correlation between 'engine-size' and 'price'


# Scatterplot

sns.regplot(x='engine-size', y='price', data=df)        # Engine size as potential predictor variable of price
plt.ylim(0,)


# Pearson correlation

from scipy import stats     # to get the P-value

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  



# ANALYSIS OF VARIANCE ANOVA

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val)  















