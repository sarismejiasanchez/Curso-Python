# 11. Copiar listas en Python sin compartir memoria con slicing

a = [1, 2, 3, 4, 5]
b = a
print(a) # [1, 2, 3, 4, 5]
print(b) # [1, 2, 3, 4, 5]

# Modifying 'a' also modifies 'b' because both refer to the same list in memory
del a[0]
print(a) # [2, 3, 4, 5]
print(b) # [2, 3, 4, 5]

# Checking memory addresses
print(id(a))    # 133101780830656
print(id(b))    # 133101780830656 (same as id(a))

# Creating a copy of 'a' using slicing
c = a[:]
print(id(a))    # 133487956806080
print(id(b))    # 133487956806080
print(id(c))    # 133487954657152

# Modifying 'a' does not affect 'c'
a.append(6)
print(a)    # [2, 3, 4, 5, 6]
print(b)    # [2, 3, 4, 5, 6]
print(c)    # [2, 3, 4, 5]