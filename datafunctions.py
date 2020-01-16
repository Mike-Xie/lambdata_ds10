 import string
 import numpy 

print("data functions")

"""
toy function returns an integer increased a number by 1 

x : int -> int
"""
def increment(x):
	return(x + 1)

"""
toy function, strips punctuation

text : string -> string
"""
def strip_punctuation(text):
	exclude = string.strip_punctuation
	return ''.join(s for s in text if s not in exclude)

