#!/usr/bin/python

import sys
import re # for regular expressions

# -------------------------- Mathematical functions --------------------------
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

# ---------------------------- Parsing functions ----------------------------

# Regex explanation:
# We are looking for a substring which:
# 1) [\+\-]?	-->	starts with ['+' or '-']. '?' specifies that it starts
#					with only 0 or 1 occurence of '+' or '-'
#					(Example: in string "+-+-+-24" we will get "-24")
# 2) .			--> indicates the start of the next rule
#					(we are no more looking for '+' or '-')
# 3) [\d\.\d]*.	--> next section of the string must be composed of:
# 					'\d' stands for digits, \. = '.' (so digits, '.', digits)
# 					'*' specifies that any number of occurences can be present
#					(-42.24576864 or 0 both satisfy the pattern)
# 4) [\s\*]+.	--> next section is composed of spaces and characters '*'
#					'\s' stands for "spaces". Any number of occurrences is
#					accepted
#					'+' stands for "at least one occurence of spaces or '*' must be there"
# 5) {1}X\^		--> next section is composed of exactly one occurence
# 					of "X^" + str(current_exponent)
# 					current exponent starts at 0 and goes up (X^0, X^1 etc)
def	get_regex(current_exponent):
	ret = "[\+\-]?.[\d\.\d]*.[\s\*]+.{1}X\^" + str(current_exponent)
	return (ret)

# This function is responsible for finding the highest exponent present in the polynome
# Example" "5 * X^0 + 4 * X^1 - 9.3 * X^18 = 1 * X^0" --> will return "18"
def	get_highest_exponent(polynome):
	regex = ".{1}X\^.[\d\d]*"
	regex_result = re.findall(regex, polynome)
	regex2 = "[\d]+"
	c_max = 0
	for i in range (0, len(regex_result)):
		regex_sub_result = re.findall(regex2, regex_result[i])
		expo_found = int(regex_sub_result[0])
		if (expo_found > int(c_max)):
			c_max = expo_found
	return (int(c_max))

def	get_variables():
	polynome = sys.argv[1]
	exp = 0
	ex_max = get_highest_exponent(polynome)
	while (exp <= ex_max):
		my_regex = get_regex(exp)
		f0 = re.findall(my_regex, polynome)
		print(exp, f0)
		exp+=1
		

def	main():
	if (len(sys.argv) != 2):
		print("Program arguments error")
		return
	get_variables()

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
if __name__ == "__main__":
	main()
