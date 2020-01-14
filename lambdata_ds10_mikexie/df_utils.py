"""
utility functions for working with Dataframes
"""
import pandas as pd 
import numpy as np 
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn import train_test_split

"""
creates a confusion matrix dataframe from a model's y_true and y_pred values
"""
def confusion_matrix_df(y_true, y_pred):
	data = confusion_matrix(y_true, y_pred)
	index = ['Predicted True', 'Predicted False']
	columns = ['Reality True', 'Reality False']
	return pd.DataFrame(data, index, columns)

"""
creates a greenscale confusion matrix from a model's y_true and y_pred values
"""
def plot_confusion_matrix(y_true, y_pred):

	index = ['Predicted True', 'Predicted False']
	columns = ['Reality True', 'Reality False']

	table = pd.DataFrame(
		confusion_matrix(y_true, y_pred), columns=columns, index=index
		)
	return sns.heatmap(table, annot=True, fmt='d', cmap='Greens')

"""
wrapper function to call train_test_split twice, 
splits val and test evenly from whatever leftover from train
"""
def train_val_test_split(df, train_size= 0.6):


	if len(df) <3:
		# return error if df has less than 3 items
		return -1
	else:
		train, temp = train_test_split(df, test_size=train_size)
		val, test = train_test_split(temp, test_size=0.5)
		return train, val, test


def add_list_as_col(df, lis):
	pass


def add_list_as_row(df, list):
	pass



def models_runner(models, features, target):
	# for model in models:
	# 	model.fit(train[features], train[target])
	pass




class Character:

	def __init__(self, name):
		self.name = name
		self.perks =[]
		self.job = "unemployed"
		self.status = "healthy"

	def add_perks(self, perk):
		self.perks.append(perk)

	def change_job(self, job):
		self.job = job

	def get_sick(self, status):
		self.status = "sick"