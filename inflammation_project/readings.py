import numpy

import loaddata

import sys


def main():
	
filename=sys.argv[1]
	
data = loaddata.load(filename)
	
print("I am learning github")
print(filename)
	
print(data.mean(axis=1))



main()
