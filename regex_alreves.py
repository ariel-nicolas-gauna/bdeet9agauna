import re

with open("archivo.txt", "r", encoding="utf-8") as archivo_entrada:
    contenido = archivo_entrada.readlines()  

with open("archivo_reverso.txt", "w", encoding="utf-8") as archivo_salida:
    for linea in contenido:
        linea_invertida = re.sub(r"(.*)", lambda m: m.group(1)[::-1], linea)
        
        archivo_salida.write(linea_invertida)