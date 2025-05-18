import re

with open("archivo.txt", "r", encoding="utf-8") as archivo_entrada:
    contenido = archivo_entrada.readlines()

contenido_sin_vacias = [linea for linea in contenido if not re.match(r"^\s*$", linea)]

with open("archivo_sin_vacias.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.writelines(contenido_sin_vacias)

print("Las líneas vacías han sido eliminadas y guardadas en 'archivo_sin_vacias.txt'.")