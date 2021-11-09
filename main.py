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

# Returns the sign of float/int argument
def	sign(f):
	f_abs = abs(f)
	if (f / f_abs == -1):
		return (-1)
	return (1)

def	sign_char(f):
	if (sign(f) == -1):
		return ('-')
	return '+'

def	first_elem_sign(f):
	if (sign(f) == -1):
		return ('-')
	return ('')
# ---------------------------- Parsing functions ----------------------------

# Regex explanation:
# We are looking for a substring which:
# 1) [\+\-]?	-->	starts with ['+' or '-']. '?' specifies that it starts
#					with only 0 or 1 occurence of '+' or '-'
#					(Example: in string "+-+-+-24" we will get "-24")
# 2) [\s]*		--> followed by any amount of spaces
# 3) [\d]+		-->	next section of the string must be composed of:
# 					at least one digit
# 4) [\.]?[\d]* -->	next section will be composed of 0 or 1 '.' chars
#					and any amount of digits
# 4) [\s\*]+.	--> next section is composed of spaces and characters '*'
#					'\s' stands for "spaces". at least 1 occurrence is accepted
#					'+' stands for "at least one occurence of spaces or '*' must be there"
# 5) X\^n{1}		--> next section is composed of exactly one occurence
# 					of "X^" + str(current_exponent)
# 					current exponent starts at 0 and goes up (X^0, X^1 etc)
def	get_regex(current_exponent):
	base_coeff = "[\+\-]?[\s]*[\d]+[\.]?[\d]*[\s\*]+X\^" + str(current_exponent) + "{1}"
	with_coefficients = base_coeff + "[\s]?" + "|" + base_coeff + "$"

	base_no_coeff = "[\+\-]?[\s]*X\^" + str(current_exponent)
	without_coefficients = base_no_coeff + "[^\d]" + "|" + base_no_coeff + "$"

	ret = with_coefficients + "|" + without_coefficients
	return (ret)

# This function is responsible for finding the highest exponent present in the polynome
# Example" "5 * X^0 + 4 * X^1 - 9.3 * X^18 = 1 * X^0" --> will return "18"
def	get_highest_exponent(polynome):
	regex = ".{1}X\^.[\d]*.[\s]*"
	regex_result = re.findall(regex, polynome)
	print(regex_result)
	regex2 = "[\d]+"
	c_max = 0
	lis = list()
	for i in range (0, len(regex_result)):
		regex_sub_result = re.findall(regex2, regex_result[i])
		lis.append(regex_sub_result)
	return (int(max(lis)[0]))

# This function will return the float which multiplies X^Something
# Example: for a string "-4.79 * X^34" it will return a float "-4.79"
def	get_the_coefficient(expr):
	result = 0
	expr_no_spaces = expr.strip()
	regex = "^[\+\-]?[\s]*[\d]+[\.]?[\d]*"
	found = re.findall(regex, expr_no_spaces)
	if (found):
		temp = str(found).strip("[\']")
		result = "".join(temp.split())
	return (float(result))

# This function is responsible for the simplified form of the equation
def	print_simplified_equation(lst):
	equation = ""
	for i in range(0, len(lst)):
		elem = lst[i]
		if elem:
			sgn = first_elem_sign(elem)
			space = ''
			if (i):
				sgn = sign_char(elem)
				space = ' '
			if elem.is_integer():
				elem = int(elem)
			equation += (str(sgn) + space + str(abs(elem)) + " * X^" + str(i) + " ")
	print("Reduced form: " + equation)

# Reads the string and stores variables in a dictionnary
def	get_variables(polynome):
	pol_split = polynome.split("=", 1)
	ex_max = get_highest_exponent(polynome)
	exp = 0
	coefficient = 0
	lst = []
	while (exp <= ex_max):
		my_regex = get_regex(exp)
		before_equal = re.findall(my_regex, pol_split[0])
		after_equal = re.findall(my_regex, pol_split[1])
		for i, s in enumerate(before_equal):
			plus = get_the_coefficient(before_equal[i])
			if (plus):
				coefficient += plus
		for i, s in enumerate(after_equal):
			minus = get_the_coefficient(after_equal[i])
			if (minus):
				coefficient -= get_the_coefficient(after_equal[i])
		lst.append(coefficient)
		coefficient = 0
		print(exp, before_equal, "=", after_equal)
		exp+=1
	print(lst)
	print_simplified_equation(lst)
	

def	main():
	if (len(sys.argv) != 2):
		print("Program arguments error")
		return
	get_variables(sys.argv[1])

if __name__ == "__main__":
	main()
