print("Ejemplo números pares")
print("Número inicial")
inicio = int(input())
print("Número final")
fin = int(input())
# Realizamos el bucle por rango
for i in range(inicio, fin + 1):
    # Preguntamos si el número es par
    if (i % 2 == 0):
        # Tenemos un par
        print(i)
print("Fin de programa")