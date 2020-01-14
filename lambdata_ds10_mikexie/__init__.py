"""
lambdata - a collection of data science helper functions
"""

import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split

# check dataframe for nulls

ONES_LIST = [1,1,1]
ONES = pd.DataFrame(np.ones(10))

 
"""
 train/validate/test split for the dataframe
"""
def train_val_test_split(df):
    train, test = train_test_split(df, train_size = 0.8, test_size = 0.2)
    val, test = train_test_split(test, test_size = 0.5)
    return train, val, test


# create confusion matrix 




# append list to dataframe

# def df_append_list(df, list):
