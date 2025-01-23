# 7. Todo lo que Debes Saber sobre print en Python

# 1. Uso básico de print
print("Nunca Pares De Aprender!")
print("Never Stop Learning!")

# 2. Uso de la coma en print
print("Nunca", "Pares", "De", "Aprender")   # Nunca Pares De Aprender

# Concatenación (+)
print("Nunca" + "Pares" + "De" + "Aprender")   # NuncaParesDeAprender
print("Nunca" + " " + "Pares" + " " + "De" + " " + "Aprender")  # Nunca Pares De Aprender

# 3. Uso de sep
print("Nunca", "Pares", "De", "Aprender", sep=", ")   # Nunca, Pares, De, Aprender
print("Nunca", "Pares", "De", "Aprender", sep="-")  # Nunca-Pares-De-Aprender

# 4. Uso de end
print("Nunca", end=" ")
print("pares de aprender")  # Nunca pares de aprender

print("Nunca", end="/")
print("pares de aprender")  # Nunca/pares de aprender

# 5. Impresión de variables
sentence = "Nunca Pares De Aprender"
author = "Platzi"
print("Frase:", sentence, "Autor:", author) # Frase: Nunca Pares De Aprender Autor: Platzi

# 6. Uso de formato con f-strings
sentence = "Nunca Pares De Aprender"
author = "Platzi"
print(f"Frase: {sentence}, Autor: {author}") # Frase: Nunca Pares De Aprender, Autor: Platzi

# 7. Uso de formato con format
sentence = "Nunca Pares De Aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(sentence, author))  # Frase: Nunca Pares De Aprender, Autor: Platzi
print("Frase: {}, Autor: {}".format(author, sentence))  # Frase: Platzi, Autor: Nunca Pares De Aprender

# 8. Impresión con formato específico
valor = 3.14159
print("Valor: {:.2f}".format(valor))    # Valor: 3.14
print("Valor: {:.4f}".format(valor))    # Valor: 3.1416

# 9. Saltos de línea y caracteres especiales
print(f"{sentence}\n{author}")  # Nunca Pares De Aprender
                                # Platzi

print("Hola soy \'Sara\'")  # Hola soy 'Sara'
print("Hola soy \"Sara\"")  # Hola soy "Sara"
print("La ruta del repositorio es: \\workspaces\\Curso-Python") # La ruta del repositorio es: \workspaces\Curso-Python\

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 25-26: truncated \UXXXXXXXX escape
# print("La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt")    