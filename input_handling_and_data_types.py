# 9. Entrada de información y manejo de tipos de datos en Python

# The data type of the input function is always a string (str).
name = input("What is your name? ")
print(f"Hello {name}")
print(type(name))   # <class 'str'>

# Casting
age = int(input("How old are you? ")) # Casting to int
#age = float(input("¿Cuántos años tienes? ")) # Casting to float
print(f"Your age is {age}")
print(type(age))    # <class 'int'>

# When we enter a different data type than expected, it generates the following error:
# ValueError: invalid literal for int() with base 10: 'Sara'