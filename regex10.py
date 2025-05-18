import re

texto = "ba9 be7 ab5 xb2"
palabras = re.findall (r'\bb[aeiou]\d\b', texto)

print(palabras)