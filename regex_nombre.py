import re

# Pedir al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")

# Expresión regular para validar que el nombre tenga solo letras y espacios, y empiece con mayúscula
patron_nombre = r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*$"

# Validar el nombre con regex
if re.match(patron_nombre, nombre):
    # Abrir el archivo 'nombres.txt' en modo escritura (añadir)
    with open("nombres.txt", "a", encoding="utf-8") as archivo:
        archivo.write(nombre + "\n")
    print(f"El nombre {nombre} ha sido guardado en 'nombres.txt'.")
else:
    print("El nombre ingresado no es válido. Asegúrate de que empiece con mayúscula y solo contenga letras.")