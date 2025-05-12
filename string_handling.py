# 5. Manejo de Cadenas y Operaciones Básicas en Python

# The Strings in Python can be defined using single quotes, double quotes, or triple quotes.

# str -> string
# Double quotes
name = "Platzi"
print(type(name))   # <class 'str'>
print(name)   # Platzi

# Single quotes
name = 'Platzi'
print(type(name))   # <class 'str'>
print(name)   # Platzi

# Triple quotes
# Triple quotes are used for multi-line strings
name = '''Platzi'''
print(type(name))   # <class 'str'>
print(name)   # Platzi

name = """Platzi
    Python"""
print(type(name))   # <class 'str'>
print(name)   # Platzi \n   Python

# Indexing
# Indexing is used to access individual characters in a string
# The first character has index 0, the second character has index 1, and so on.
name = "Sara Mejía"
print(name[0])  # S
print(name[1])  # a
print(name[2])  # r
print(name[3])  # a

# print(name[20])  IndexError: string index out of range

# Indexing negative
# The last character has index -1, the second to last character has index -2, and so on.
print(name[-1]) # a
print(name[-2]) # í

# Concatenation
# Concatenation is used to join two or more strings together
name = "Sara Maria"
last_name = "Mejía Sánchez"

print(name)   # Sara Maria
print(name + last_name) # It concatenates the two strings without space
print(name + " " + last_name)   # It concatenates the two strings with space

# Repetition
# Repetition is used to repeat a string a certain number of times
print(name * 5) # Repeats the string 5 times

# Length
# The length of a string is the number of characters in the string
print(len(name))    # 10
print(len(last_name))   # 13

# Methods
# The methods of a string are functions that can be used to manipulate the string
name = "SARA"
last_name = "   Mejía   Sánchez "

print(name.lower()) # sara
print(name.upper()) # SARA
print(last_name)    #    Mejía   Sánchez
print(last_name.strip())    # Mejía   Sánchez, removes spaces at the beginning and end

"""
# The methods of a string are functions that can be used to manipulate the string:
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
eval()
exec()
"""