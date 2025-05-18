import re 

def mayus(cadena):
    regex = r'^[A-Z][a-z]+$'
    return bool(re.match(regex, cadena))

print(mayus("hola"))
print(mayus("Hola"))
print(mayus("HoLa"))