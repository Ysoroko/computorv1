# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ysoroko <ysoroko@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 11:31:15 by ysoroko           #+#    #+#              #
#    Updated: 2021/11/10 11:41:34 by ysoroko          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all: test1

# 1) As given in the subject (1 X^0 on the right side of "=")
#	Solution:
#	Discriminant is strictly positive, the two solutions are:
#	[0.905239]
#	[-0.475131]
test1:
	python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 18 * X^0"

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
	python3 main.py "42 ∗ X^0 = 42 ∗ X^0"

# 5) All of the components cancel out (Reduced form: 0 = 0)
#	Solution: [all the "reals"]
test5:
	python3 main.py "42 ∗ X^0 + 13.46 * X^1 - 1 * X^2 = 42 ∗ X^0 + 13.46 * X^1 - 1 * X^2"

# 6) Check to see how the equation balances out
#	Solution: 
test6:
	python3 main.py "42 * X^0 + 3.5 * X^1 - 0.256 * X^2 = 41 * X^0 + 1.75 * X^1 + 0.256 * X^2"

#--------------------------------- ERROR CASES -----------------------------------
# 5) Negative exponent ( = invalid polynome)
test_error1:
	python3 main.py "42 ∗ X^-2 - 3 * X^-1 + 1.4 * X^0 - 5 * X^1 + 3 * X^2 = 1.789 ∗ X^0"

# 6) No "=" sign
test_error2:
	python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2"



