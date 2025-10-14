# 12. Manejo de Matrices y Tuplas en Python

# Creating a matrix (list of lists)
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0])    # [1, 2, 3]
print(matrix[2][2]) # 9

# Adding elements
matrix.append([10, 11, 12])
print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Create a tuple
numbers = (1, 2, 3, 4, 5)
print(numbers)  # (1, 2, 3, 4, 5)
print(type(numbers))    # <class 'tuple'>

# Accessing elements in a tuple
print(numbers[2])   # 3

# Tuples are immutable
# numbers[0] = "unos" # TypeError: 'tuple' object does not support item assignment

# Creating a tuple without parentheses
other_tuple = 4, 5, 6, 7, 8
print(other_tuple)  # (4, 5, 6, 7, 8)
print(type(other_tuple))    # <class 'tuple'>