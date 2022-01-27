# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ysoroko <ysoroko@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 11:31:15 by ysoroko           #+#    #+#              #
#    Updated: 2022/01/27 17:18:54 by ysoroko          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all: test1

# 1) As given in the subject (1 X^0 on the right side of "=")
#	Solution:
#	Discriminant is strictly positive, the two solutions are:
#	[0.905239]
#	[-0.475131]
test1:
	python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

# 2) As given in the subject (1 X^0 on the right side of "=")
#	Solution: [-0.25]
test2:
	python3 main.py "5 * X^0 + 4 * X^1 = 4 * X^0"

# 3) As given in the subject (1 X^0 on the right side of "=")
#	Solution: [degree > 2, can't solve]
test3:
	python3 main.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

# 4) As given in the subject
#	Solution: [all the "reals"]
test4:
	python3 main.py "42 * X^0 = 42 * X^0"

# 5) All of the components cancel out (Reduced form: 0 = 0)
#	Solution: [all the "reals"]
test5:
	python3 main.py "42 * X^0 + 13.46 * X^1 - 1 * X^2 = 42 * X^0 + 13.46 * X^1 - 1 * X^2"

# 6) Check to see how the equation balances out
#	Solution: [3.916642] [-0.498673]
test6:
	python3 main.py "42 * X^0 + 3.5 * X^1 - 0.256 * X^2 = 41 * X^0 + 1.75 * X^1 + 0.256 * X^2"

# 7) Coefficients cancel out in the middle
#	 Negative coefficient, complex solutions only!
#	 The complex solutions are:
#	 ( - i * sqrt(-483.6) ) / -18.6
#	 ( i * sqrt(-483.6) ) / -18.6
#	Solution:
test7:
	python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 18 * X^0 + 4 * X^1"

# 9) Complex solutions
#	x2 + 4x + 5 = 0
#	The complex solutions are:
#	( -4 - i * sqrt(-4) ) / 2
#	( -4 + i * sqrt(-4) ) / 2
test8:
	python3 main.py "5 * X^0 + 4 * X^1 + 1 * X^2 = 0"

# 10) Complex solutions
# 	x2 - 3x + 10 = 0
# 	The complex solutions are:
# 	( 3 - i * sqrt(-31) ) / 2
# 	( 3 + i * sqrt(-31) ) / 2
test9:
	python3 main.py "10 * X^0 - 3 * X^1 + 1 * X^2 = 0"


# 9) X^2 with a null coefficient
#	Simplified version should be: [4 * X^0 + 3 * X^1 - 1 * X^2]
#	Solutions are: [4][-1]
test10:
	python3 main.py "4 * X^0 + 3 * X^1 - X^2 = 0"
#--------------------------------- ERROR CASES -----------------------------------
# 1) Negative exponent ( = invalid polynome)
test_error1:
	python3 main.py "42 * X^-2 - 3 * X^-1 + 1.4 * X^0 - 5 * X^1 + 3 * X^2 = 1.789 ∗ X^0"

# 2) No "=" sign
test_error2:
	python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2"

# 3) Chars different from [spaces, digits, '.', '+', '-', '*', '=' 'X', '^']
test_error3:
	python3 main.py "A * X^0 + 32,4 * X^1 = 1 * X^0"

# 4) Annoying "∗" char (!!! ----> ["∗" != "*"])
test_error4:
	python3 main.py "42 ∗ X^0 = 42 ∗ X^0"


