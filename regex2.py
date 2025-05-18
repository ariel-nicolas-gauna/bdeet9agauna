import re

def solo_numeros (cadena):
    regex = '^[1-20]+$'
    return bool(re.match(regex, cadena))

print(solo_numeros("123"))
print(solo_numeros("12a45"))
print(solo_numeros("19"))