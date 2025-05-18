import re

def solo_minusculas(cadena):
    regex = r'^[a-z]+$'
    return bool(re.match(regex, cadena))


print(solo_minusculas("hola"))       
print(solo_minusculas("Hola123"))    
print(solo_minusculas("holamundo"))  
print(solo_minusculas("HOLA"))       
print(solo_minusculas("hola mundo")) 
