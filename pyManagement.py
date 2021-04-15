'''


Reference websites for pandas:
    https://pandas.pydata.org/
    https://pandas.pydata.org/pandas-docs/stable/reference/index.html

'''


# IMPORT LIBRARIES

import pandas as pd                 
import numpy as np
import matplotlib.pylab as plt      


# IMPORT DATASET (.csv file with no header!) 

df_path = "C:/Users/lione/myPythonPrograms/ACTUAL_dta_analysis/data/auto.csv"
df = pd.read_csv(df_path, header=None)

df_can = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)


# Read/Save Other Data Formats

#Data   Formate     Read                Save

#       csv	        pd.read_csv()       df.to_csv()
#       json        pd.read_json()      df.to_json()
#       excel       pd.read_excel()     df.to_excel()
#       hdf         pd.read_hdf()       df.to_hdf()
#       sql         pd.read_sql()       df.to_sql()



# CREATE A TABLE BASED ON A DICTIONARY

BMI = {'name':['Lionel','François','Jules'],'date':['01/02/2021','02/03/2021','03/04/2021'],'weight':[77,81,85],'height':[184,184,184]}

bmi_frame = pd.DataFrame(BMI)   #Create a table based on a dictionary

bmi_frame.head()



# DESCRIBE DATASET

df.head()                   # print first rows
df['price'].head(10)

df.tail()                   # print last rows

df.describe()               # returns a statistical summary
df.describe(include=['object'])     # to apply the method on the variables type 'object'
df.describe(include='all')  # provides a full summary statistics

df.dtypes()

df.info()
df.info(verbose=False)      # verbosebool, optional = Whether to print the full summary.

df.columns                  # list of column headers we can call upon the dataframe'
df.columns.values
print(df.columns)

df['drive-wheels'].unique() # group the variable "drive-wheels" by categories

df.index.values             # the list of indicies
print(df.index)

print(df.shape)                    # shows the dimensions of the dataframe  

print(type(df.columns))     # columns default type >> The default type of columns is NOT list.
print(type(df.index))       # index default type >> The default type of index is NOT list.

df_can.columns.tolist()     # get the columns as lists
df_can.index.tolist()       # get the index as lists

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))

# example
print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)



# SELECT COLUMNS

# There are two ways to filter on a column name:

# Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.

df.column_name              # returns series
df_can.Country              # for example returns the column Country


# Method 2: More robust, and can filter on multiple columns.

df_group_one = df[['drive-wheels','body-style','price']]        # returns dataframe
df.head()

x = df['body-style']        # get the column as a series

df.drop(['drive-wheels','body-style','price'], axis=1, inplace=True)    # # in pandas axis=0 represents rows (default) and axis=1 represents columns.
df.head()

df_dropped = df.drop(['drive-wheels','body-style','price'], axis=1) # create a new table instead of inpleace
df_dropped.head()



# RENAME COLUMNS

df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df.columns

# convert column names into strings

all(isinstance(column, str) for column in df_can.columns)   # let's examine the types of the column labels

df_can.columns = list(map(str, df_can.columns))     # [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

# Since we converted column to string, let's declare a variable that will allow us to easily call upon the full range of years:

years = list(map(str, range(1980, 2014)))       # useful for plotting later on
print(years)




# SELECT ROW

#Before we proceed, notice that the defaul index of the dataset is a numeric range from 0 to n. This makes it very difficult to do a query by a specific key. For example to search for data on a employee, we need to know the corressponding index value. This can be fixed very easily by setting the 'Employee' column as the index using set_index() method.

df_firm.set_index('Employee', inplace=True)     # tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()

df_firm.index.name = None     # optional: to remove the name of the index


#MANY WAYS TO SELECT DATA FROM A DATA FRAME IN PANDAS

df.loc[label]                 # filters by the labels of the index/column

df.iloc[index]                # filters by the positions of the index/column


#Example: Let's VIEW the number of immigrants from Japan (row 87) for the following scenarios:

# 1. The full row data (all columns)
print(df_can.loc['Japan'])

# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())


# 2. for year 2013
print(df_can.loc['Japan', 2013])

# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36


# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])    # returns a dataframe
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])      # notice that 'Country' is string, and the years are integers. for the sake of consistency, we will convert all column names to string later on.
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])


# get the top 5 entries
df_top5 = df_top.head(5)



#THREE WAYS TO SELECT DATA FROM A DATA FRAME IN PANDAS

#There are main 3 ways to select rows:

df.loc[label]               # filters by the labels of the index/column
df.iloc[index]              # filters by the positions of the index/column

'''
Before we proceed, notice that the defaul index of the dataset is a numeric range from 0 to n. This makes it very difficult to do a query by a specific country. For example to search for data on Japan, we need to know the corressponding index value.

This can be fixed very easily by setting the 'Country' column as the index using set_index() method.
'''

df_can.set_index('Country', inplace=True)    # tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.index.name = None    # optional: to remove the name of the index


# 1. the full row data (all columns)
print(df_can.loc['Japan'])

# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())


# 2. for year 2013
print(df_can.loc['Japan', 2013])

# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36


# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])



#loc is primarily label based; uses column headers and row indexes to select the data. loc can also take an integer as a row or column number.
bmi_frame.loc[1,'name']                             #Find the element in the second-row and first column


#iloc is integer-based. Use column numbers and row numbers to get rows or columns at particular positions in the data frame. 
bmi_frame.iloc[1,0]                                 #Find the element in the second-row and first column


#ix looks for a label. If ix doesn't find a label, it will use an integer. In Pandas version 0.20.0 and later, ix is deprecated


#USE LOC AND ILOC TO SLICE DATA FRAMES AND ASSIGN THE VALUE TO A NEW DATA FRAME

sample = bmi_frame.loc[0:1,'name':'weight']         #Using loc for slicing.

sample = bmi_frame.iloc[0:2,0:3]                    #Using iloc for slicing.



#~DISTINCT
new_frame = bmi_frame['name'].unique()              #Values without duplicates


#~SELECT
bmi_frame['weight']>= 79                            #Result is a True / False for each line

new_frame = bmi_frame[bmi_frame['weight']>=79]      #Define a new table following the criteria


#~SORT
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)    # a little bit different
df_can.head()


#~TRANSPOSE
years = list(map(str, range(1980, 2014)))
df_top5 = df_can.head()
df_top5 = df_top5[years].transpose() 



# FILTERING BASED ON A CRITERIA

# To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)


# 2. pass this condition into the dataFrame
df_can[condition]


# 3. we can pass mutliple criteria in the same line. 
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or' # don't forget to enclose the two conditions in parentheses



# COUNTS

df['num-of-doors'].value_counts()       # which values are present in a particular column

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()      # convert the series to a Dataframe and save the results to the dataframe "drive_wheels_counts"
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace = True)  # rename the column 'drive-wheels' to 'value_counts'
drive_wheels_counts.index.name = 'drive-wheels'     # rename the index to 'drive-wheels
print(drive_wheels_counts)


df['num-of-doors'].value_counts().idxmax()  # calculate the most common type automatically:



# TOTAL

df_can['Total'] = df_can.sum(axis=1)        # add a 'Total' column that sums up the total per line over the differents columns



# IDENTIFY AND HANDLE MISSING VALUES

# There are several methods to detect missing data

missing_data = df.isnull()
missing_data.head(5)            # "True" stands for missing value, while "False" stands for not missing value.

nonmissing_data = df.notnull()  # "False" stands for missing value, while "True" stands for not missing value.
nonmissing_data.head(5)


df.isnull().sum()               # how many null objects we have


# Count missing values in each column

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")   


# Replace missing values

df1 = df.replace('?',np.NaN)                    # replace missing values '?' with Nan NaN : Not a Number
df.replace("?", np.nan, inplace = True)         # setting the argument in place to true, allows the modification to be done on the data set directly
df = df.replace('?',np.NaN)                     # df = df : also modifies the data set directly


# Replace missing values by the means

mean = df['normalized-losses'].mean()           # calculate the mean
df['normalized-losses'].replace(np.nan, mean)   # replace the missing values by the mean

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)


# Replace the missing values by the most frequent

max_doors = df['num-of-doors'].value_counts().idxmax()
df["num-of-doors"].replace(np.nan, max_doors, inplace=True)
df["num-of-doors"].replace(np.nan, "four", inplace=True)


# Remove missing values - drop rows

df2=df.dropna(subset=['price'], axis=0)     # drops the entire row

df.dropna(subset=['price'], axis=0, inplace = True)         # setting the argument in place to true, allows the modification to be done on the data set directly
df = df.dropna(subset=['price'], axis=0, inplace = True)    # df = df : also modifies the data set directly

df.reset_index(drop=True, inplace=True)     # reset index, because we droped rows


# Remove missing values - drop columns

df2=df.dropna(subset=['price'], axis=1)     # drops the entire column 'price'



# DATA FRAME OPERATIONS

df['column1'] = df[column1] + 1

df['new_city-mpg'] = 235/df['city-mpg']     # transforms miles/gallons into liters/100km

df.rename(columns={'new_city_mpg': 'city_L/100km'}, inplace = True)     # rename a column



# DATA FORMATING

df.dtypes()     # to identify data type
df.astype()     # to convert data type


# Convert data types to proper format

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")



# DATA NORMALIZATION

# Replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()



# DATA BINNING

bins = np.linspace(min(df['price']), max(df['price']),4)    # defines 4 equally spaced numbers over the minimum and maximum of the price
group_names = ['Low','Medium','High']                       # group_names contains the different bin names

df.['price-binned'] = pd.cut(df['price'], bins, labels=group_names, include_lowest = True)      # segment and sort the data values into bins



# TURNING CATEGORICAL VALUES TO NUMERIC VARIABLES : 'one-hot encoding'

dummy_variable_1 = pd.get_dummies(df["fuel-type"])          # get indicator variables and assign it to data frame "dummy_variable_1
dummy_variable_1.head()

dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)     # change column names for clarity
dummy_variable_1.head()

df = pd.concat([df, dummy_variable_1], axis=1)              # merge data frame "df" and "dummy_variable_1" 

df.drop("fuel-type", axis = 1, inplace=True)                # drop original column "fuel-type" from "df"



# SAVE DATASET

df.to_csv("C:/Users/lione/myPythonPrograms/ACTUAL_dta_analysis/data/new_auto.csv", index=False)


# Read/Save Other Data Formats

#Data   Formate     Read                Save

#       csv	        pd.read_csv()       df.to_csv()
#       json        pd.read_json()      df.to_json()
#       excel       pd.read_excel()     df.to_excel()
#       hdf         pd.read_hdf()       df.to_hdf()
#       sql         pd.read_sql()       df.to_sql()


