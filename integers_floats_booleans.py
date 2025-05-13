# 6. Tipos de Datos en Python: Enteros, Flotantes y Booleanos

x = 10
print(x)
print(type(x))  # <class 'int'>

y = 5.432
print(y)
print(type(y))  # <class 'float'>

# The Scientific notation is used to represent very large or very small numbers.
z = 1.2e6
print(z)        # 1200000.0
print(type(z))  # <class 'float'>

a = 1E6
print(a)        # 1000000.0
print(type(a))  # <class 'float'>

b = 1.2E-6
print(b)        # 1.2e-06
print(type(b))  # <class 'float'>

print(f"x: {x}, y: {y}, z: {z}, a: {a}, b: {b}")  # x: 10, y: 5.432, z: 1200000.0, a: 1000000.0, b: 1.2e-06
print(x + x)    # 20
print(x + y)    # 15.432
print(y + y)    # 10.864
print(z + a)    # 2200000.0

# Booleans
is_true = True
print(is_true)  # True
print(type(is_true))    # <class 'bool'>

is_false = False
print(is_false) # False
print(type(is_false))   # <class 'bool'>

# https://chatgpt.com/share/679288da-0260-8003-8555-6ca278de58ca
x = 10 
y = 5.123 
print(x + y)    # 15.123000000000001

print(round(x + y, 3))  # 15.123

from decimal import Decimal
# Using Decimal for precise decimal arithmetic
x = Decimal('10.0')
y = Decimal('5.123')
print(x + y)    # 15.123