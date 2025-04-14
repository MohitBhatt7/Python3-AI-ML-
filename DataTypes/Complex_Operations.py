# Addition of the complex numbers.

z1 = 2 + 3j
z2 = 4 + 3j

Sum = z1 + z2
print("The sum of the complex numbers in z1 and z2 is:- ", Sum)

# Substraction of the complex number

Difference = z2 - z1
print("The difference between z2 and z2 is:- ", Difference)

# Multiplication of the complex number.

Z1 = 3 + 2j
Z2 = 5 + 7j

Multiplication = Z1 * Z2
print("The value for multiplication of Z1 and Z2", Multiplication)


# Division of two complex number.

A1 = 2 + 8j
A2 = 1 + 4j

Division = A1/A2
print("The value for division is:- ", Division)

# Here in the method of division Python uses formula:-  (a + bj)/(c + dj) = {(ac + bd) + (bc - ad)}j/(c^2 + d^2)

# Modulus of the complex number.

magnitude = abs(z2)
print("The magnitude of z1 is :- ", magnitude) 

# Conjugate of complex number.
conjugate = z1.conjugate()
print("The conjugate of z1 is:- ", conjugate)

# To print the real and imaginary part of the complex number.
print(z1.real)
print(z1.imag)

# Working of the expontiation.

A = z1 ** 2
print(A) # This works on formu;a of (a + b)^2