# Assigning the value of x.

x = 5

# Small change (i.e h)
h = 0.000001

fx = 3 * x**2 + 2
fx_h = 3 * (x + h)**2 +2

#Derivative Approximation
Derivative = (fx_h - fx)/h
print("DErivative is:- ", Derivative)