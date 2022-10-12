import matplotlib.pyplot as plt

def leer_columna_csv(n_columna,archivo):
    if not archivo.startswith(".."):
        archivo="..\\csv\\"+archivo
    if not archivo.endswith(".csv"):
        archivo=archivo+".csv"
    with open(archivo, 'r') as f:
        datos = []
        for line in f:
            columnas = line.split(',')
            datos.append(columnas[n_columna])
        return datos

def leer_datos_csv(nom):
    if not nom.startswith(".."):
        nom="..\\csv\\"+nom
    if not nom.endswith(".csv"):
        nom=nom+".csv"
    with open(nom, 'r') as f:
        resultado = []
        for line in f:
            columnas = line.split(',')
            fila=[]
            for i in range(len(columnas)):
                fila.append(columnas[i])
            resultado.append(fila)
        return resultado

preguntas=["Edad actual","Edad cuando sintió gusto o atracción física por primera vez por una persona","Edad tenía cuando tuvo su primer encuentro con alguien donde haya habido besos o caricias, y que usted estuviera de acuerdo","Edad de su primera relación sexual","Edad en que se dio cuenta de su orientación sexual"]
columnas=[1,55,56,60,74]

for i in range(len(preguntas)):
    datos=leer_columna_csv(columnas[i],"conjunto_de_datos_tmodulo_endiseg_web_2022.csv")
    datos.pop(0) # quitamos el nombre de la columna
    datos=[int(i) for i in datos if isinstance(i, int) or (isinstance(i, str) and i.isnumeric())] # convertimos todo a integer
    datos=sorted(datos)
    bins = 100
    plt.hist(datos, bins, (0,99), color = 'green', histtype = 'bar', rwidth = 0.8)
    plt.xlabel('Edad')
    plt.ylabel("Num.Personas")
    plt.title(preguntas[i], loc='center', wrap=True)
    #plt.show()
    plt.savefig(preguntas[i]+'.png')