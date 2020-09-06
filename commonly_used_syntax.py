# Created on Sunday, 6th September 2020
# 09:10:17 GMT+7

__author__ = "airlangga fidiyanto"


####################
# Importing Stuffs #
####################

import pandas as pd
import numpy as np
import matplotlib as plt

my_file_path = 'path_to_my_data.csv'

################
# Reading Data #
################

df = pd.read_csv(my_file_path) # for other file types visit Panda's documentation on IO tool's (https://bit.ly/2FeohAz)

####################
# Data Exploration #
####################

# returns (row, column)
df.shape

# returns first 5 data or  first n data(s) if head(n)
df.head()

# similar as head but it's n last data(s)
df.tail()

# return an object consist of column headers
df.columns

# basic information of all columns
df.info()

# basic statistic information of numeric column
df.describe()

# show dataframe's data type of each column
df.dtypes

# show which values are null
df.isnull()

# show which column(s) that have null value(s)
df.isnull().any()

# show the percentage of null value(s)
df.isnull().sum() / data.shape[0]

# plot histogram for all numeric column(s)
df.hist()
