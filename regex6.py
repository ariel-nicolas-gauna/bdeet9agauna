import re

def variable(cadena):
  regex = r'^[A-Za-z_][A-Za-z0-9_]'
  return bool(re.match(regex, cadena))

print(variable("_ariel2"))
print(variable("@ari"))
