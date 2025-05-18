import re

def validar_fecha(fecha):
    regex = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    return bool(re.match(regex, fecha))

print(validar_fecha("10/05/2025"))  
print(validar_fecha("32/01/2023")) 
print(validar_fecha("5/5/2025"))    