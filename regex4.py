import re

texto = "1 45 123 2025 123456"
numeros = re.findall(r'\b\d{2,4}\b', texto)
print(numeros)