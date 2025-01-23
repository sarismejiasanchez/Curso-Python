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

# print(name[20])  IndexError: string index out of range

# Recorrer desde el final
print(name[-1]) # a
print(name[-2]) # a

# Concatenación
name = "Sara Maria"
last_name = "Mejía Sánchez"

print(name)
print(name + last_name) # No se agrega un espacio entre los valores de la cadenas
print(name + " " + last_name)   # Se agrega espacio entre valores de la cadenas

# Repetición
print(name * 5) # Repite el valor de la cadena 5 veces

# Longitud
print(len(name))    # 10
print(len(last_name))   # 13

# Métodos
name = "SARA"
last_name = "   Mejía   Sánchez "

print(name.lower()) # sara
print(name.upper()) # SARA
print(last_name)    #    Mejía   Sánchez
print(last_name.strip())    # Mejía, elimina los espacios en blanco al principio y final de la cadena

"""
Algunos métodos para cadenas son:
.count() 
.capitalize()
.title() 
.swapcase() 
.replace(,) 
.split() 
.strip() 
.lstrip() 
.rstrip() 
.find()
.index() 
eval()	#Este y el siguiente son super métodos
exec()
"""