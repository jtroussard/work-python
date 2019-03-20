#!/usr/bin/python3

"""description"""

__author__      = "Jacques Troussard"

import os,sys

try:
	with open(".\???!!!\ouput.json", "w") as out, open(".\???!!!\input.txt", "r") as inp:
		for line in inp:
			print(line)
	
except:
	print("Unexpected error: When starting program: ", sys.exc_info()[0])
	raise
