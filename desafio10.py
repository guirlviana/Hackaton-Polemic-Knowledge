import math
a = int(input("Qual o valor de A: "))
b = int(input("Qual o valor de B: "))
c = int(input("Qual o valor de C: "))

delta = (b ** 2) - 4 * a * c
Rdelta = math.sqrt(delta)
x1 = (-b + Rdelta) / 2 * a
x2 = (-b - Rdelta) / 2 * a
print(f"Delta: {delta}")
print(f"X1: {x1}")
print(f"X2: {x2}")