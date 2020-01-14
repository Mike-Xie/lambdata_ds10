"""
utility functions for working with Dataframes
"""
import pandas as pd 
import numpy as np 
from sklearn.metrics import confusion_matrix
import seaborn as sns

"""
creates a confusion matrix from a model's y_true and y_pred values
"""

def confusion_matrix_df(y_true, y_pred):
	data = confusion_matrix(y_true, y_pred)
	index = ['Predicted True', 'Predicted False']
	columns = ['Reality True', 'Reality False']
	return pd.DataFrame(data, index, columns)


def plot_confusion_matrix(y_true, y_pred):

    index = ['Predicted True', 'Predicted False']
    columns = ['Reality True', 'Reality False']

    table = pd.DataFrame(confusion_matrix(y_true, y_pred), columns=columns, index=index)
    return sns.heatmap(table, annot=True, fmt='d', cmap='Greens')

def train_val_test_split(df, train_size= 0.6, val_size=0.2):
	total_len = len(df.index)

	first_split_index = int(train_size * total_len)
	second_split_index = int(val_size * total_len) + first_split_index

	train = df.iloc[df[:first_split_index]] 
	val = df.iloc[df[first_split_index:second_split_index]] 
	test = df.iloc[df[second_split_index:]] 
	
	return train, val, test

	
	