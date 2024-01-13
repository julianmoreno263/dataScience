# booleanos
lista = []
edades = [13, 15, 20]


def verifica(lista, edades):
    for edad in edades:
        if edad >= 18:
            lista.append(True)
        else:
            lista.append(False)
    for ver in lista:
        if ver == True:
            print("Usted puede conducir")
        else:
            print("Usted no puede conducir")


verifica(lista, edades)

print(lista)


# ------------------------------------------------------------

print("-------------------------------------")

persona = ["maria", 25, True, "mexico"]

for elemento in persona:
    print(f"El elemento {elemento} de la lista es del tipo ", type(elemento))


# ------------------------------------------------------------
