import pandas as pd


# -------------------------------------------------
# BIBLIOTECA PANDAS PARA DATA SCIENCE

# pandas tiene unas estructuras de datos para manipular los datos

# 1- series: son arrays unidimensionales capaces de almacenar cualquier tipo de objeto.Es como si fuera una tabla de una unica columna,cada fila tendra una etiqueta llamada index.Para crear una serie es sencillo, invocamos la clase Series de la biblioteca pandas y esta pide el array de datos y el index,podemos hacerlo asi:

carros = ["audi", "renault", "chevrolet", "mazda"]

s = pd.Series(carros)
print(s)

# 2- dataframes: son estructuras de datos bidimensionales,almacenan cualquier tipo de datos,si por ejemplo tenemos una tabla de mas de una columna utilizamos los dataframes.Podemos pasar tambien cualquier tipo de dato en el dataframe,incluso otro dataframe,ademas le podemos pasar el index e indices para las columnas,usamos la clase Dataframe, el resultado sera una tabla donde las llaves seran los nombres de las columnas y los valores formaran las respectivas filas:

datos = [
    {"nombre": "audi", "motor": "diesel 300", "year": 2023},
    {"nombre": "chevrolet", "motor": "diesel 300", "year": 2012},
    {"nombre": "renault", "motor": "diesel v8", "year": 2015},
]

dt = pd.DataFrame(datos)

print(dt)

# 3-puedo crear un dataframe a partir de un diccionario:
dic = {
    'nombre': ['jetta', 'audi', 'renault'],
    'motor': ['diesel 300', 'diesel 300', 'diesel v8'],
    'year': [2023, 2012, 2015],
}

df = pd.DataFrame(dic)
print(df)

# 4-puedo crear un dataframe a partir de un archivo externo,como una bd externa,que sera los mas comun:
df = pd.read_csv('Pandas\data\db.csv', sep=';')
print(df)
