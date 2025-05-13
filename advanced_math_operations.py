# 8. Operaciones matemáticas avanzadas en Python: módulo, potencia y más

# Numerical operations in Python
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Exponenciación:", a ** b)

# ZeroDivisionError: division by zero
#b = 0
#print(a / b)

# Shortcuts
a += 2
print(a)

a -= 2
print(a)

a *= 2
print(a)

a /= 2
print(a)

a //= 3
print(a)

a %= 2
print(a)

a **= 2
print(a)

# PEMDAS
# Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right)
print("PEMDAS")
operation_1 = 2 + 3 * 4
print(operation_1)
operation_2 = 2 + (3 * 4)
print(operation_2)
operation_3 = (2 + 3) * 4
print(operation_3)
operation_4 = (2 + 3) * (4 ** 2) / 8 - 1 # (5) * (16) / 8 - 1 = 80 / 8 = 10 - 1 = 9
print(operation_4)

# Boolean operations
print("Boolean operations")
a = 10
b = 3

print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False
print(a == b)   # False
print(a != b)   # True
