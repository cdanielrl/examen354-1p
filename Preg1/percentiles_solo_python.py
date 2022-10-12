def percentil_num(datos,p):
    tam=len(datos)
    ordenado=sorted(datos)
    n=((p/100)*tam)
    n=round(n)
    elem=ordenado[n]
    return n,elem

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
    resp=percentil_num(datos,25)
    print("Primer cuartil "+preguntas[i]+" : "+str(resp[1])+" posicion: "+str(resp[0]))
    resp=percentil_num(datos,90)
    print("Percentil 90 "+preguntas[i]+" : "+str(resp[1])+" posicion: "+str(resp[0]))
    resp=percentil_num(datos,95)
    print("Percentil 95 "+preguntas[i]+" : "+str(resp[1])+" posicion: "+str(resp[0]))