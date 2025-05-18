import re
texto = "programacion regex hello keyboard"
palabras = re.findall(r'\b[a-zA-Z]{5}\b', texto)

print(palabras)