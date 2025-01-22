# 5. Manipulación de Cadenas de Texto en Python

# str -> string
name = "Platzi"
print(type(name))   # str

name = 'Platzi'
print(type(name))   # str

name = '''Platzi'''
print(type(name))   # str

name = """Platzi
Python"""
print(type(name))   # str

# indexacion
name = "Sara Mejía"
print(name[0])  # S
print(name[1])  # a
print(name[2])  # r
print(name[3])  # a
print(name[20])  #  IndexError: string index out of range
