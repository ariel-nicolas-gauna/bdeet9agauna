import re


def calcular_costo(mensaje):
    costo_total = 0
    
    
    letras = re.findall(r"[a-zA-Z]", mensaje)
    costo_total += len(letras) * 10  

    
    digitos = re.findall(r"\d", mensaje)
    costo_total += len(digitos) * 20  

    
    especiales = re.findall(r"[^a-zA-Z0-9\s]", mensaje)
    costo_total += len(especiales) * 30 

    return costo_total


mensaje = input("Ingresa el mensaje: ")


costo = calcular_costo(mensaje)


print(f"El costo para enviar el mensaje es: ${costo}")