numeros = [4, 15, 2, 30, 8, 11, 5]

suma_total = sum(numeros)

mayores_que_diez = len([n for n in numeros if n > 10])

cuadrados = [n**2 for n in numeros]

mayor = max(numeros)

print("Suma total:", suma_total)
print("Cantidad de números mayores que 10:", mayores_que_diez)
print("Lista de cuadrados:", cuadrados)
print("Mayor número:", mayor)