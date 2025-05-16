# 10. Manipulación de Listas en Python: Creación, Indexación y Métodos Básicos

to_do = [
    "Go to the hotel",
    "Go to lunch",
    "Visit a museum",
    "Return to the hotel"
]

print(to_do)

numbers = [1, 2, 3, 4, "5"]
print(numbers)  # [1, 2, 3, 4, '5']
print(type(numbers))    # <class 'list'>

# Created list from a string
texto = list("Hello World")
print(texto)    # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

mix = ["uno", 2, 3.1416, True, [1, 2, 3]]
print(mix)  # ['uno', 2, 3.1416, True, [1, 2, 3]]
print(type(mix))    # <class 'list'>

# Counting elements in a list
print(len(mix)) # 5

# Indexing
print("Indexing")
print(f"First item: {mix[0]}") # First item: uno
print(f"Second item: {mix[1]}") # Second item: 2
print(f"Last item: {mix[-1]}") # Last item: [1, 2, 3]

for item in range(len(mix)):
    print(f"Item {item}: {mix[item]}")
    
# Indexing with strings
name = "Sara Mejia"
print(name[0]) # S
print(name[5]) # M

# Slicing
print(mix[0: 2])    # ['uno', 2]
print(mix[3:])  # [True, [1, 2, 3]]
print(name[5:]) # Mejia
print(name[: 5]) # Sara

# Methods
print("\nMethods")
print(mix)

# Add item to the end of the list
mix.append(False)
print(mix)

mix.append(["a", "b"])
print(mix)

# Add item to specific position
mix.insert(3, ["a", "b"])
print(mix)

# Search for an item in the list
print(mix.index(["a", "b"])) # 3, this item is at multiple positions, but returns the first one

# Find the maximum and minimum values in a list
numbers = [1.5, 2, 100, 90, 45, 3]
print(numbers)
print(f"Max: {max(numbers)}")   # Max: 100
print(f"Min: {min(numbers)}")   # Min: 1.5

# Delete an item from the list
numbers.remove(1.5)
print(numbers)

# Delete the last item
numbers.pop() # 3
print(numbers)

# Delete an item by index
del numbers[-2] # 90
print(numbers)

# Delete a range of items
del numbers[0: 2] # [2, 100]
print(numbers)

# Delete the entire list
del numbers
#print(numbers) # NameError: name 'numbers' is not defined