import re

# Abrir el archivo en modo lectura
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()  # Leer todo el contenido del archivo

# Contar el número de líneas
lineas = contenido.splitlines()  # Dividir el contenido en líneas
num_lineas = len(lineas)

# Usar regex para contar el número de palabras (cualquier secuencia de letras o números)
patron_palabra = r'\b\w+\b'
num_palabras = len(re.findall(patron_palabra, contenido))

# Contar el número de caracteres (todos los caracteres, incluyendo saltos de línea)
num_caracteres = len(contenido)

# Mostrar los resultados
print(f"El archivo tiene:")
print(f"- {num_lineas} líneas")
print(f"- {num_palabras} palabras")
print(f"- {num_caracteres} caracteres")