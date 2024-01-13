# generar numeros aleatorios entre 0 y 10 y almacenarlos en una lista, usaremos una biblioteca para esto.Se puede importar toda la biblioteca utilizando import,o solo un modulo de esta utilizando from "biblioteca" import "modulo", importaremos el modulo randrange de la biblioteca random.

from random import randrange

# esta es otra forma de importar un modulo de una biblioteca,en este caso importamos el paquete pyplot de la biblioteca matplotlib, y se acostumbra poner un alias corto a ese paquete.Hay que instalar esa biblioteca via pip asi: pip install matplotlib.
from matplotlib import pyplot as plt

notas_alumno = []

# con range le decimos que el ciclo solo se ejecuta cierta cantidad de veces y asi no queda un bucle infinito
for notas in range(6):
    notas_alumno.append(randrange(0, 11))

print(notas_alumno)
print(len(notas_alumno))  # aqui veo el tamaño de la lista

# graficar las notas,primero generamos los datos del grafico en su eje horizontal,el vertical seran las notas
x = list(range(1, 7))
y = notas_alumno

# aqui creamos la grafica,para que se muestre debemos usar el emtodo show()
plt.plot(x, y, marker="o")  # marker pone los puntos en la linea principal
plt.title("Gráfico de notas del alumno")
plt.xlabel("Pruebas")
plt.ylabel("Notas alumno")
plt.show()
