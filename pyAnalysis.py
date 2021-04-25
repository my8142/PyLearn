'''

Other Plots
There are many other plotting styles available other than the default Line plot, all of which can be accessed by passing kind keyword to plot().

The full list of available plots are as follows:

    bar                 for vertical bar plots
    barh                for horizontal bar plots
    hist                for histogram
    box                 for boxplot
    kde or density      for density plots
    area                for area plots
    pie                 for pie plots
    scatter             for scatter plots
    hexbin              for hexbin plot

Reference websites for matplotlib:
    http://www.aosabook.org/en/matplotlib.html
    https://matplotlib.org/stable/index.html
    https://matplotlib.org/?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork-20297740&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork-20297740&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ


'''




# IMPORT LIBRARIES

import pandas as pd
import numpy as np



# INSTALL SEABORN ON JUPYTER

%%capture
! pip install seaborn



# IMPORT VISUALIZATION PACKAGE

import seaborn as sns

# Matplotlib
%matplotlib inline              # to plot in a Jupyter notebook !
import matplotlib as mpl
import matplotlib.pyplot as plt

print ('Matplotlib version: ', mpl.__version__) # optional: check if Matplotlib (version >= 2.0.0) is loaded

print(plt.style.available)      # optional: apply a style to Matplotlib.
mpl.style.use(['ggplot'])       # optional: for ggplot-like style


# CATEGORICAL DATA

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels':'value_counts'}, inplace = True)
print(drive_wheels_counts)



# LINE PLOTS

#Example

# 1. Extract the data series for Haiti
haiti = df_can.loc['Haiti', years] # previously years as been defined as a list of several variables passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()


# 2. plot a line plot by appending .plot() to the haiti dataframe
haiti.plot()


# 3. let's label the x and y axis using plt.title(), plt.ylabel(), and plt.xlabel()
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')


# 4. let's annotate the 2010 Earthquake spike in the plot by using the plt.text() method.
plt.text(2000, 6000, '2010 Earthquake') # syntax: plt.text(x, y, label)


# 5. change the size using the `figsize` parameter.
haiti.index = haiti.index.map(int) # let's change the index values of haiti to type integer for plotting
haiti.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size


# 6. show the updates made to the figure
plt.show() # need this line to plot again


'''
We can easily add more countries to line plot to make meaningful comparisons immigration from different countries: Let's compare the number of immigrants from India and China from 1980 to 2013.
'''

df_CI = df_can.loc[['India', 'China'], years]     # example for 2 countries

'''
That doesn't look right...?

That's because unlike for series (like haiti) dataframe has the years as its indices.

Recall that _pandas_ plots the indices on the x-axis and the columns as individual lines on the y-axis. Since `df_CI` is a dataframe with the `country` as the index and `years` as the columns, we must first transpose the dataframe using `transpose()` method to swap the row and columns.
'''

df_CI = df_CI.transpose()
df_CI.head()

'''
_pandas_ will auomatically graph the two countries on the same graph. Go ahead and plot the new transposed dataframe. Make sure to add a title to the plot and label the axes.
'''

df_CI.plot(kind='line')
plt.title('Immigration from China & India')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()


# AREA PLOTS

# Created a dataframe of the top 5 countries that contribued the most immigrants to Canada from 1980 to 2013

df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head()

# transpose the dataframe
df_top5 = df_top5[years].transpose() 
df_top5.head()


df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='area', 
             alpha=0.25, # 0-1, default value a= 0.5 // transparency
             stacked=False,
             figsize=(20, 10),
            )

df_top5.plot(kind='area', stacked=False, figsize=(20, 10), # pass a tuple (x, y) size)
'''
Area plots are stacked by default. And to produce a stacked area plot, each column must be either all positive or all negative values (any NaN values will defaulted to 0). To produce an unstacked plot, pass stacked=False.
'''


plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# PIE CHARTS

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%',   # autopct create %, start angle represent starting point
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12) 

plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

plt.show()





# HISTOGRAMS

count, bin_edges = np.histogram(df_canada['2013'])  # split the distribution into 10 bins of equal width

df_can['2013'].plot(kind='hist', xticks = bin_edges)

plt.title('Histogram of Immigration from 195 countries in 2013')
plt.ylabel('Number of countries')
plt.xlabel('Number of immigrants')

plt.show()


# BAR CHARTS

years = list(map(str, range(1980, 2014)))
df_iceland = df_canada.loc['Iceland', years]

df_iceland.plot(kind='bar')

plt.title('Icelandic immigrants to Canada from 1980 to 2013')
plt.xlabel('Year')
plt.ylabel('Number of immigrants')

plt.show()


# BOX PLOTS

sns.boxplot(x='drive-wheels', y='price', data=df)

df_japan = df_canada.loc[['Japan'], years].transpose()
df_japan.plot(kind='box')

plt.title('Box plot of Japanese Immigrants from 1980-2013')
plt.ylabel('Number of Immigrants')

plt.show()


# SCATTER PLOT

df_total.plot(kind = 'scatter', x = 'year', y = 'total',)

plt.title('Total Immigrant population to Canada from 1980-2013')
plt.xlabel('Year')
plt.ylabel('Numer of immigrants')

plt.show()


# Another solution ?

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















