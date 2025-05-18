import os

carpeta = 'c:/ruta/a/la/carpeta'# Reemplaza con la ruta real

archivos = [arch for arch in os.listdir(carpeta) if os.path.listfile(os.path.join(carpeta, arch))]

archivos.sort()

for i, nombre_original in enumerate(archivos, start=1):
    ruta_original = os.path.join(carepta, nombre_original)
    nuevo_nombre = f"{i}_{nombre_original}"
    ruta_nueva = os.path.join(carepta, nuevo_nombre)
    os.rename(ruta_original, ruta_nueva)

print("renombrado completo")