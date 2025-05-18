import re

texto = "ba9 be7 ab5 xb2 bo5 bu3"
coincidencias = re.findall (r'\bb[aeiou]\d\b', texto)

print(coincidencias)