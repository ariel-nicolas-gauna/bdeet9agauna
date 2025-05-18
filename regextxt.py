import os

carpeta = 'c:/ruta/a/la/capeta'
archivos_txt = [arch for arch in os.listdir(carpeta) if arch.endswith('.txt')]

if archivos_txt:
    print("se han encontrado estsps archivos:")
    for archivo in archivos_txt:
      print(archivo)

    confirmacion = input("¿usted desea eliminar estos archivos? (s/n) :").strip().lower()

    if confirmacion == 's':
      for archivo in archivos_txt:
        ruta_completa = os.path.join(carpeta, archivo)
      os.remove (ruta_completa)
      print('archivos .txt eliminados')
    else:
       print('operacion cancelada')
       
else:print('no se encontraron archivos .txt en la carpeta')

