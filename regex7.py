import re

def correo(cadena):
    regex = r'^\b[\w.-]+@[\w.-]+\.\w+\b'
    return bool(re.match(regex, cadena))

print(correo("arielnicolasgauna3@gmail.com"))