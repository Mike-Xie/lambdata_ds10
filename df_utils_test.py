import unittest

import df_utils 

class DataframeTests(unittest.TestCase):
	""" tests df train val test split function"""
	def test_train_val_test_split(self):
		test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

		a, b, c = df_utils.test_train_val_test_split(test_list, 0.6, 0.2)

		self.assertEqual(len(a), 6)
		self.assertEqual(len(b), 2)
		self.assertEqual(len(c), 2)
if __name__ == '__main__':
	unittest.main()