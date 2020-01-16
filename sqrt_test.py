import unittest

import square_root as sr 
from math import sqrt

class SqrtTests(unittest.TestCase):
	"""tests square root functions"""
	def test_sqrt9(self):
		self.assertEqual(sr.newton_sqrt(9), 3)

	def test_sqrt2(self):
		self.assertEqual(sr.lazy_sqrt(2), sqrt(2))	

if __name__ == '__main__':
	unittest.main()
