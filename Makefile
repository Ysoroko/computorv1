# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ysoroko <ysoroko@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 11:31:15 by ysoroko           #+#    #+#              #
#    Updated: 2021/11/09 11:39:49 by ysoroko          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all: test1

# 1) As given in the subject (1 X^0 on the right side of "=")
#	Solution:
#	Discriminant is strictly positive, the two solutions are:
#	[0.905239]
#	[-0.475131]
test1:
	python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 + X^0 = 1 * X^0"

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

