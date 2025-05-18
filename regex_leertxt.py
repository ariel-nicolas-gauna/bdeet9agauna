import re

# Abrimos el archivo
with open("texto.txt", "r", encoding="utf-8") as archivo:
    for i, linea in enumerate(archivo, start=1):
        # Buscar teléfonos y nombres en cada línea
        telefonos = re.findall(r"\b\d{2,3}-\d{3,4}-\d{4}\b", linea)
        # Ahora solo capturamos palabras de más de 1 letra que empiezan con mayúscula
        nombres = re.findall(r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*\b", linea)

        # Mostrar los resultados
        print(f"Línea {i}: {linea.strip()}")
        if telefonos:
            print("  Teléfonos encontrados:", telefonos)
        if nombres:
            print("  Nombres encontrados:", nombres)