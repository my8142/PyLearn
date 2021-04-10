
# IMPORT LIBRARIES
# http://pandas.pydata.org
# https://pandas.pydata.org/pandas-docs/stable/reference/index.html
# http://www.aosabook.org/en/matplotlib.html
import pandas as pd                 
import numpy as np
import matplotlib.pylab as plt      


# IMPORT DATASET (.csv file with no header!) 

df_path = "C:/Users/lione/myPythonPrograms/ACTUAL_dta_analysis/data/auto.csv"
df = pd.read_csv(df_path, header=None)


# Read/Save Other Data Formats

#Data   Formate     Read                Save

#       csv	        pd.read_csv()       df.to_csv()
#       json        pd.read_json()      df.to_json()
#       excel       pd.read_excel()     df.to_excel()
#       hdf         pd.read_hdf()       df.to_hdf()
#       sql         pd.read_sql()       df.to_sql()



# DESCRIBE DATASET

df.head()                   # print first rows
df['price'].head(5)

df.tail()                   # print last rows

df.describe()               # returns a statistical summary
df.describe(include=['object'])     # to apply the method on the variables type 'object'
df.describe(include='all')  # provides a full summary statistics

df.dtypes()

df.info()
df.info(verbose=False)

df.columns
df.columns.values

df['drive-wheels'].unique() # group the variable "drive-wheels" by categories

df.index.values

df.shape    



# SELECT COLUMNS

df_group_one = df[['drive-wheels','body-style','price']]
df.head()

x = df['body-style']        # get the column as a series

df.drop(['drive-wheels','body-style','price'], axis=1, inplace=True)



# RENAME COLUMNS

df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df.columns



# CREATE A TABLE BASED ON A DICTIONARY

BMI = {'name':['Lionel','François','Jules'],'date':['01/02/2021','02/03/2021','03/04/2021'],'weight':[77,81,85],'height':[184,184,184]}

bmi_frame = pd.DataFrame(BMI)   #Create a table based on a dictionary

bmi_frame.head()



#THREE WAYS TO SELECT DATA FROM A DATA FRAME IN PANDAS

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



# COUNTS

df['num-of-doors'].value_counts()       # which values are present in a particular column

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()      # convert the series to a Dataframe and save the results to the dataframe "drive_wheels_counts"
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace = True)  # rename the column 'drive-wheels' to 'value_counts'
drive_wheels_counts.index.name = 'drive-wheels'     # rename the index to 'drive-wheels
print(drive_wheels_counts)


df['num-of-doors'].value_counts().idxmax()  # calculate the most common type automatically:



# IDENTIFY AND HANDLE MISSING VALUES

# There are two methods to detect missing data

missing_data = df.isnull()
missing_data.head(5)            # "True" stands for missing value, while "False" stands for not missing value.

nonmissing_data = df.notnull()  # "False" stands for missing value, while "True" stands for not missing value.
nonmissing_data.head(5)


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


