import re

texto = "abcdefghijklmnÑopqrstuvwxyz"
letras = re.findall (r'[e-o]', texto)

print(letras)