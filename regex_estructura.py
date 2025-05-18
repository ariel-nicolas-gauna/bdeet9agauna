import re  

texto = "Mi correo es juan@capo.com y la fecha de hoy es 2025-05-12."

variable_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

variable_fecha = r"\d{4}-\d{2}-\d{2}"

correos = re.findall(variable_email, texto)

fechas = re.findall(variable_fecha, texto)

print("Correos encontrados:", correos)
print("Fechas encontradas:", fechas)