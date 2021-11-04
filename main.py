#!/usr/bin/python

import sys

def	abs(n):
	if (n >= 0):
		return n
	return -n

def	sqrt(n):
	x = n
	y = 1
	error = 0.00000000000000001
	while (x - y > error):
		x = (x + y) / 2
		y = n / x
	return (x)

def	main():
	f1 = float(sys.argv[1])
	print(sqrt(f1))

if __name__ == "__main__":
	main()