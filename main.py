#!/usr/bin/python

import sys
import re # for regular expressions

def	abs(n):
	if (n >= 0):
		return n
	return -n

# Babylonian Method
# 1) Guess a number for square root value
# 2) Set a margin of error
# 2) Add 1 to our guess number and divide it by 2
# 3) Repeat until our guess fits in the margin of error
def	sqrt(n):
	x = n
	y = 1
	error = 0.00000000000000001
	while (x - y > error):
		x = (x + y) / 2
		y = n / x
	return (x)

def	get_variables():
	polynome = sys.argv[1]
	exp = 0
	f0 = 1

	while (f0):
		my_regex = "[\d\.\d]+.{1}\*.{1}X\^" + str(exp)
		f0 = re.findall(my_regex, polynome)
		print(exp, f0)
		exp+=1
		

def	main():
	if (len(sys.argv) != 2):
		print("Program arguments error")
	get_variables()

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
if __name__ == "__main__":
	main()