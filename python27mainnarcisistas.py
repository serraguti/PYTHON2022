import python27metodosnarcistas

print("Ejemplo narcisista y bisiesto")
print("1.- Bisiesto")
print("2.- Narcisista")
print("Seleccione una opción")
print("---------------------")
opcion = int(input())
if (opcion == 1):
    print("Introduzca un año")
    anyo = int(input())
    respuesta = python27metodosnarcistas.isBisiesto(anyo)
    if (respuesta == True):
        print("El año es bisiesto")
    else:
        print("Año NO bisiesto")
elif (opcion == 2):
    print("Introduce un número")
    textoNumero = input()
    respuesta = python27metodosnarcistas.isNarcisista(textoNumero)
    if (respuesta == True):
        print("Es un número narcisista")
    else:
        print("Lo siento, su número NO es narcisista")
else:
    print("Opción incorrecta")
print("Fin de programa")
