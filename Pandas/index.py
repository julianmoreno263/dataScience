# aprender a manejar datos con pandas

import pandas as pd


pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 7)

# leer el archivo con los datos, esto sera un array,dataset es un dataframe,osea un objeto que sirve para almacenar datos que viene de un archivo o bd.
dataset = pd.read_csv("Pandas\data\db.csv", sep=';')


print("------------------------------------------")

# imprimir el tipo de dato de cada columna
print(dataset.dtypes)

print("------------------------------------------")

# mostrar estadisticas de dos columnas,como la mediana,la desviacion standar,el valor minimo y maximo,porcentaje en  cuartiles.
print(dataset[["Kilometraje", "Valor"]].describe())

print("------------------------------------------")

# mostrar informacion de nuestro dataset
print(dataset.info())

print("------------------------------------------")


# tuplas en python, son colecciones de objetos inmutables,osea las tuplas no permiten cambiar una vez se hayan creado.Pueden almacenar objetos de diferente tipo.Las tuplas van con () y las listas con [].

miTupla = ("ana", 32, True)
print(type(miTupla))

# para recorrer o manipular los elementos de la tupla lo hacemos como un array comenzando desde la posicion 0.
tupla2 = tuple(["renault", "mazda", "chevrolet", "audi"])
print(tupla2[0])

# si quiero comenzar a contar desde el ultimo elemento hacia adelante,uso el -1.
print(tupla2[-1])

# si quiero capturar un grupo de elementos especificos en la tupla le paso la posicion inicial y la posicion final mas 1,por ejemplo quiero mostrar mazda y chevrolet,chevrolet es la posicion 2 pero debo llamar es a la 3 para que me capture el 2.
print(tupla2[1:3])

# si tengo una tupla dentro de otra y quiero acceder a un elemento de la tupla hija debo accesar por orden,primero acceso a la posicion de la tupla hija y luego accedo a la posicion del elemento de esa tupla hija. Por ejemplo accederemos al elemento sail de la tupla hija.
tupla3 = ("renault", "mazda", "chevrolet", "audi",
          ("logan", "mazda 3", "sail", "a4"))
print(tupla3[-1][2])


print("------------------------------------------")

# iterando tuplas con for in
for item in tupla2:
    print(item)

print("------------------------------------------")

# desempacando tuplas
car1, car2, car3, car4 = tupla2

print(car1)
print(car2)
print(car3)
print(car4)

print("------------------------------------------")

# si solo quiero guardar los elementos con posicion 1 y 4 de la tupla,ignoro las variables con un _
_, car2, _, car4 = tupla2
print(car2)
print(car4)

print("------------------------------------------")

# si tengo una tupla con 100 elementos, y solo quiero capturara uno,puedo indicar que los otros seran ignorados poniendo un *_
_, car2, *_ = tupla2
print(car2)

print("------------------------------------------")

# funcion zip() crea un iterador con tuplas, primero creamos dos listas y despues iteramos estas listas con la funcion zip(), despues las mostramos con la funcion list(), aparecera una lista de tuplas con los valores combinados.
list1 = ["renault", "mazda", "chevrolet", "audi"]
list2 = [345000, 435000, 235000, 560000]
result = zip(list1, list2)
for item in result:
    print(item)

print("------------------------------------------")

# puedo desempaquetar esas tuplas y despues hacer operaciones con esos datos,por ejemplo mostrar solo los carros con un precio mayor a 350000
for carro, valor in zip(list1, list2):
    if (valor > 350000):
        print(carro, valor)


print("------------------------------------------")

# los diccionarios en python son una estructura de datos que agrupa elementos en parejas de clave y valor.Para acceder al elemento se necesita conocer la clave.Los diccionarios se crean entre {}.
datos = {"renault": 345000, "mazda": 435000,
         "chevrolet": 235000, "audi": 560000}

print("------------------------------------------")

# puedo crear diccionarios de otra forma,usando zip() y la funcion dict(),con zip creo el array de tuplas y despues ese array lo puedo pasar a diccionario con dict() el cual se encargara de hacer las parejas de clave y valor.
datos = dict(zip(list1, list2))
print(datos)

print("------------------------------------------")

# para acceder al valor de un elemento del diccionario simplemente ponemos el nombre del diccionario y entre [] la clave del elemento.
print(datos["renault"])

print("------------------------------------------")

# para saber si una clave esta en el diccionario se pone key in diccionario,esto dara true o false.
print("pepe" in datos)  # aqui da false porque no existe la clave "pepe"

print("------------------------------------------")

# para saber el tamaño o numero de elementos de un diccionario es con len() y le pasamos el diccionario,esto es util en diccionarios grandes.
print(len(datos))

print("------------------------------------------")

# para adicionar un elemento a un diccionario es asi:
datos["jeep"] = 450000
print(datos)

print("------------------------------------------")

# para eliminar un elemento de un diccionario es asi:
del datos["jeep"]
print(datos)

print("------------------------------------------")

# metodos de los diccionarios, metodo update() para actualizar el diccionario,pdemos volver a agregarle elementos al diccionario con este metodo tambien se puede cambiar valores de los elementos,etc,porque el actualiza los diccionarios
datos.update({"jep": 450000})
datos.update({"jeep": 500000, "citroen": 190000})

# para eliminar elementos del diccionario uso del asi:
del datos["jep"]

print(datos)

print("------------------------------------------")

# metodo copy(),crear una copia del diccionario original
datosCopy = datos.copy()

print(datos)

print("------------------------------------------")

# metodo pop(),tambien sirve para eliminar un elemento, si el elemento no existe nos devuelve un mensaje personalizado, si el elemento si existe lo elimina y nos muestra el valor que tenia.
datosCopy.pop("citroen")

# si intento eliminarlo de nuevo me saca un error por defecto,puedo personalizar ese error
datosCopy.pop("citroen", "La llave no fue encontrada")


print(datosCopy)

print("------------------------------------------")

# metodo clear(),elimina todos los items del diccionario,lo deja limpio
datosCopy.clear()

print(datosCopy)

print("------------------------------------------")

# vamos a iterar los diccionarios con los metodos especiales para ello,el primer metodo es el keys(),este metodo devuelve las llaves del diccionario,me muestra una lista con las llaves.
llaves = datos.keys()

print(llaves)

print("------------------------------------------")

# puedo mostrar estas llaves iterando sobre ealista que salio de llaves
for key in llaves:
    print(key)

print("------------------------------------------")

# el metodo values() devuelve los valores del diccionario
valores = datos.values()
for valor in valores:
    print(valor)


print("------------------------------------------")

# el metodo items() devuelve una lista de tuplas con los elementos del diccionario,parecido al metodo zip() que habiamos visto
items = datos.items()
for item in items:
    print(item)


# ahora,puedo desempacar cada una de estas tuplas, recordar que print puede llevar mas de un parametro
for key, value in items:
    print(key, "->", value)


print("------------------------------------------")

# vamos a ver las built in function, osea las funciones que ya vienen por defecto en python(para conocerlas podemos ir a https://docs.python.org/3/library/functions.html. y hay estan todas en orden alfabetico), estas son funciones que ya viene en python para ayudarnos.Ahora,por ejemplo si queremos hacer una tarea mas especifica debemos construir nuestra propia funcion,por ejemplo traer la suma de los valores de un diccionario.Pero con las built in function podemos abreviar mucho mas el codigo,por ejemplo para hacer esta suma primero creamos una lista con solo los valores del diccionario,para esto utilizamos el metodo list(datos.values()) y ya teniendo esa lista con esos valores los sumo con el metodo sum() el cual pide la lista a iterar y el parametro start=0,que es un numero que le podemos pasar e indica que la suma comenzara a partir de ese numero, este parametro es opcional.

datos = {"renault": 345000, "mazda": 435000,
         "chevrolet": 235000, "audi": 560000}

# listaSuma = list(datos.values())
# resultadoSuma = sum(listaSuma, start=0)

# se puede hacer asi con menos pasos en una sola linea
resultadoSuma = sum(datos.values())
print(resultadoSuma)

# el metodo help() me sirve para ver la descripcion de un metodo mas a fondo,por ejemplo quiero saber que hace el metodo print,utilizo help()
# help(print)

print("------------------------------------------")

# vamos a ver como crear funciones en python, para esto se utiliza la palabra reservada def(definition).Vamos a crear una funcion que calcule el promedio de unos numeros.

# definicion de la funcion


def promedio():
    valor = (1+2+3)/3
    print(valor)


# llamado de la funcion
promedio()

# --------------------------------------------
# funcion con parametros


def media(num1, num2, num3):
    valor = (num1+num2+num3)/3
    print(valor)


media(2, 5, 7)

# --------------------------------------------
# funcion que puede recibir varios parametros,no solo una cantidad fija de parametros,para esto utilizamos una lista


def mediaLista(lista):
    valor = (sum(lista))/len(lista)
    print(valor)


mediaLista([4, 8, 13, 2, 9])

# ahora, esta funcion solo imprime un resultado,pero no devuelve ningun valor porque no tiene un return,solo hace un print,por lo que esta funcion no tiene ningun tipo de dato,para que la funcion retorne algun valor y podamos manipular ese valor debe tener un return.

print("------------------------------------------")

# funcion con return


def mediaLista(lista):
    valor = (sum(lista))/len(lista)
    return valor


resultado = mediaLista([4, 8, 13, 2, 9, 67])
print(type(resultado))
print(resultado)

# -------------------------------------------------
# la funcion puede retornar mas de un valor,por ejemplo quiero devolver el valor del promedio de los numeros y la longitud de la lista, entonces esto se devuelve en una tupla asi:


def mediaLista(lista):
    valor = (sum(lista))/len(lista)
    return (valor, len(lista))


resultado = mediaLista([4, 8, 13, 2, 9, 67, 28])
print(resultado)
