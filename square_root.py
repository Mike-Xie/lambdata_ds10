def lazy_sqrt(x):
	""" Takes x and returns square root"""

	return x**0.5

def library_sqrt(x):
	"""Uses math library"""
	from math import sqrt
	return sqrt(x)

def newton_sqrt(x):
	val = x
	while True:
		last = val
		val = (val + x / val) * 0.5
		if abs(val - last) < 1e-9:
			break
	return val 

