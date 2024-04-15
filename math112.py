import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define the function
f = x**2 + 3*x + 2

# Take the derivative
f_prime = sp.diff(f, x)

# Print the derivative
print("The derivative of f(x) =", f_prime)

# Find the integral
f_integral = sp.integrate(f, x)

# Print the integral
print("The integral of f(x) =", f_integral)
