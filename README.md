# Computorv1
Polynomial equation solver, coded in Python.

![image](https://user-images.githubusercontent.com/36443074/153571769-3f15bf46-30c1-44f3-8824-3b32385a99d2.png)

### The project:

- Solves polynomial equations given as program's argument
- Balances the equation and displays the reduced form
- Displays the degree of the equation
- Computes and display the discriminant's sign when it applies
- Computes and displays the equation's solutions

### Try it:
- The Makefile present in this repository provides multiple tests
- These tests can be launched with **make testN** ('N' replaced with the number of the test)
- Example: "make test4"
- Alternatively the program accepts one string as an argument and it must be formatted in the following way:
  - "N1 * X^0 + N2 * X^1 ... Nn * X^t = M1 * X^0 + M2 * X^1 ... Mn * X^t"
  - N1 ... Nn and M1 ... Mn are the coefficients of every X
  - t is the maximum exponent of x (also the degree of the polynome)
- The program solves the equations of degrees up to 2
- The equation must be well formatted

### Useful links that helped me with this project:
- [**Regex in Python explained with examples**](https://www.w3schools.com/python/python_regex.asp)
- [**Discriminant and 2nd degree equations solving (in French)**](https://www.mathematiquesfaciles.com/solutions-complexes-d-une-equation-de-degre-2_2_45257.htm)
