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
	x = n	# our guess: square root is equal to n itself
	y = 1	# start our y at 1
	error = 0.00000000000000001 # our margin of error
	while (x - y > error):	# while our root value - our current difference is bigger than the error
		x = (x + y) / 2		# our guess is added to our difference and divided by 2
		y = n / x			# our current difference becomes our initial number, divided by our current guess
	return (x)
#	Example: sqrt(4)
#	x = 4
#	y = 1
#	error = 0.00000000000000001
#	While:
#	1)	4 - 3 > 0.00000000000000001 OK
#		x = (4 + 1) / 2 = 5 / 2 = [2.5]
#		y = 4 / 2.5 = [1.6]
#	2)	2.5 - 1.6 = 0.9 > 0.00000000000000001 OK
#		x = (2.5 + 1.6) / 2 = [2.05]
#		y = 4 / 2.05 = [1.95] (...)
#	3)	2.05 - 1.95 = 0.1 > 0.00000000000000001 OK
#		x = (2.05 + 1.95) / 2 = 4 / 2 = 2
#		y = 4 / 2 = 2
#	4)	2 - 2 = 0 > 0.00000000000000001 NO
#		return (2)

# Returns the sign of float/int argument
def	sign(f):
	f_abs = abs(f)
	if (f / f_abs == -1):
		return (-1)
	return (1)

# Returns sign in a form of a char '+' of '-'
def	sign_char(f):
	if (sign(f) == -1):
		return ('-')
	return '+'

# Returns either '' or '-' based on whether its argument is > 0 or < 0
def	first_elem_sign(f):
	if (sign(f) == -1):
		return ('-')
	return ('')

# A * X^2 + B * X^1 + C * X^0 = 0
# The discriminant is defined as:
# discriminant = B * B - (4 * A * C)
# If it's > 0 -> there are 2 possible solutions
# If it's = 0 -> there is only one possible solution
# If it's < 0 -> no real solutions possible (but complex yes)
def	get_the_discriminant(lst):
	print(lst)
	c = lst[0]
	b = lst[1]
	a = lst[2]

	discriminant = b * b - (4 * a * c)
	return (discriminant)

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
	base_coeff = "[\+\-]?[\s]*[\d]+[\.]?[\d]*[\s\*]+X\^?" + str(current_exponent) + "{1}"
	with_coefficients = base_coeff + "[\s]?" + "|" + base_coeff + "$"

	base_no_coeff = "[\+\-]?[\s]*X\^" + str(current_exponent)
	without_coefficients = base_no_coeff + "[^\d]" + "|" + base_no_coeff + "$"

	ret = with_coefficients + "|" + without_coefficients
	return (ret)

# This function is responsible for finding the highest exponent present in the polynome
# Example" "5 * X^0 + 4 * X^1 - 9.3 * X^18 = 1 * X^0" --> will return "18"
def	get_highest_exponent(polynome):
	regex = "X\^{1}[\-]?[\d]+[\s]*"
	regex_result = re.findall(regex, polynome)
	# print(regex_result)
	regex2 = "[\-]?[\d]+"
	lis = list()
	for i in range (0, len(regex_result)):
		regex_sub_result = re.findall(regex2, regex_result[i])
		lis.append(int(regex_sub_result[0]))
	return (int(max(lis)))

# This function is responsible for finding the lowest exponent present in the polynome
# Example" "5 * X^0 + 4 * X^1 - 9.3 * X^18 = 1 * X^0" --> will return "0"
def	get_lowest_exponent(polynome):
	regex = "X\^{1}[\-]?[\d]+[\s]*"
	regex_result = re.findall(regex, polynome)
	# print(regex_result)
	regex2 = "[\-]?[\d]+"
	lis = list()
	for i in range (0, len(regex_result)):
		regex_sub_result = re.findall(regex2, regex_result[i])
		lis.append(int(regex_sub_result[0]))
	return (int(min(lis)))

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
	if (equation == ""):
		equation = "0 "
	print("Reduced form: " + equation + "= 0")

# What is not a polynome:
# 1) Polynomials cannot contain division by a variable "7x/(1+x)"
# 2) Polynomials cannot contain negative exponents. "7 * X^-4"
# 3) Polynomials cannot contain fractional exponents. "7 * X ^ 4.2"
# 4) Polynomials cannot contain radicals. "7 * sqrt(X)"
def	error_found(lowest_exponent, polynome):
	if (lowest_exponent < 0):
		print("Error: polynomial expressions cannot contain negative exponents")
		return (1)
	if (polynome.find('=') == -1):
		print("Error: no \"=\" sign in the polynome expression")
		return (1)
	# Regex: anything other than spaces, digits, '.', '+', '-', '*', '=' 'X', '^'
	regex_for_wrong_chars = "[^\d^\+^\-*^\=^X\^\^^\.^\s]+"
	found_wrong_chars = re.findall(regex_for_wrong_chars, polynome)
	if (found_wrong_chars and found_wrong_chars[0]):
		print("Error: not accepted chars found in string")
		return (1)
	return (0)

# Prints the results:
# 1) Simplified equation
# 2) Polynomial degree
# 3) Discriminant
# 4) Solutions
def	print_results(lst, degree):
	equation = print_simplified_equation(lst)
	print("Polynomial degree: " + str(degree))
	if (degree > 2):
		print("The polynomial degree is stricly greater than 2, I can't solve.")
		return (False)
	return (True)

# Reads the string and stores variables in a dictionnary
def	parse(polynome):
	pol_split = polynome.split("=", 1)
	ex_max = get_highest_exponent(polynome)
	exp = get_lowest_exponent(polynome)
	if (error_found(exp, polynome)):
		return
	degree = ex_max - exp
	coefficient = 0
	lst = []
	while (exp <= ex_max):
		my_regex = get_regex(exp)
		before_equal = re.findall(my_regex, pol_split[0])
		after_equal = re.findall(my_regex, pol_split[1])
		for i in range(0, len(before_equal)):
			plus = get_the_coefficient(before_equal[i])
			if (plus):
				coefficient += plus
		if (after_equal and after_equal[0]):
			for i in range(0, len(after_equal)):
				minus = get_the_coefficient(after_equal[i])
				if (minus):
					coefficient -= get_the_coefficient(after_equal[i])
		lst.append(coefficient)
		coefficient = 0
		# print(exp, before_equal, "=", after_equal)
		exp+=1
	if (print_results(lst, degree)):
		return (lst)
	return (0)
	

def	main():
	if (len(sys.argv) != 2):
		print("Program argument must be a single polynomial expression")
		return
	list_of_coefficients = parse(sys.argv[1])
	if (not list_of_coefficients):
		return
	print(get_the_discriminant(list_of_coefficients))

if __name__ == "__main__":
	main()
