import math
import csv

def leer_columna_csv(n_columna,archivo):
    with open(archivo, 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        datos = []
        for line in csvreader:
            datos.append(line[n_columna])
        return datos

def leer_datos_csv(nom):
    with open(nom, 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        resultado = []
        for line in csvreader:
            fila=[]
            for i in range(len(line)):
                fila.append(line[i])
            resultado.append(fila)
        return resultado

def grabar_datos_csv(datos,archivo):
    with open(archivo, 'w',newline='') as f:
        write = csv.writer(f)
        write.writerows(datos)

def filtrar_csv(archivo,columnas):
    datos=[]
    resultado=[]
    nd=0
    for i in range(len(columnas)):
        col=leer_columna_csv(columnas[i],archivo)
        datos.append(col)
        if(len(col)>nd):
            nd=len(col)
    for i in range(nd):
        row=[]
        for j in range(len(columnas)):
            row.append(datos[j][i])
        resultado.append(row)
    return resultado

def eliminar_nan(datos):
    datos=[int(i) for i in datos if isinstance(i, int) or (isinstance(i, str) and i.isnumeric())]
    datos=[i for i in datos if i>0]
    return datos

def normalizar(datos):
    media = float(sum(datos)) / float(len(datos))
    de = math.sqrt(sum(pow(x-media, 2) for x in datos) / len(datos))
    resultado = [(x-media)/de for x in datos]
    return resultado


preguntas=["Edad actual","Edad cuando sintió gusto o atracción física por primera vez por una persona","Edad tenía cuando tuvo su primer encuentro con alguien donde haya habido besos o caricias, y que usted estuviera de acuerdo","Edad de su primera relación sexual","Edad en que se dio cuenta de su orientación sexual"]
columnas=[1,55,56,60,74]

print("Filtarmos solo las columnas usadas y guardamos en un archivo csv")
filtrado=filtrar_csv("..\\csv\\conjunto_de_datos_tmodulo_endiseg_web_2022.csv",columnas)
grabar_datos_csv(filtrado,"filtrado.csv")

columnas=[0,1,2,3,4]

for i in range(len(preguntas)):
    datos=leer_columna_csv(columnas[i],"filtrado.csv")
    datos.pop(0) # quitamos el nombre de la columna
    print(preguntas[i])
    print("Datos Originales")
    print(datos)
    print("Eliminando datos no numéricos y ceros")
    print(eliminar_nan(datos))
    print("Normalizando datos")
    print(normalizar(eliminar_nan(datos)))