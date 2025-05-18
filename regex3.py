import re

texto = "hola me llamo ariel"
palabras = re.findall(r'\w+', texto)
print(palabras)