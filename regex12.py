import re

texto = "Hola 123! @#"
caracteres = re.findall (r'.', texto)

print(caracteres)