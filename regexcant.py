import os 

carpeta = 'c:/ruta/a/la/carpeta'

archivos = [arch for arch in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, arch))]

cantidad = len(archivos)

print(f"Hay {cantidad} archivo(s) en la carpeta.")