import numpy
import pandas
import csv
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

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

cod_preguntas=["P4_1","P7_2","P7_3","P7_5","P8_2"]
arch_preguntas=["P7_2","P7_3","P7_5","P8_2"]
columnas=[1,55,56,60,74]
fila_diccionario_datos=[2,56,57,61,75]
preguntas=[]
tptemp=leer_columna_csv(0,"..\\csv\\diccionario_datos_tmodulo_endiseg_web_2022.csv")
for i in fila_diccionario_datos:
    preguntas.append(tptemp[i])
def_preguntas=[]
for i in arch_preguntas:
    ptemp=leer_datos_csv("..\\csv\\"+i+".csv")
    ptemp.pop()
    def_preguntas.append(ptemp)
z=zip(cod_preguntas,preguntas)
n=dict(z)

df=pandas.read_csv("..\\csv\\conjunto_de_datos_tmodulo_endiseg_web_2022.csv")
dff=df[["P8_1","P4_1","P7_2","P7_3","P7_5","P8_2"]]
dff=dff.dropna()
#print(dff)
dff.rename(columns=n,inplace=True)
b={'P8_1': 'Se considera'}
dff.rename(columns=b,inplace=True)
X=dff[preguntas]
y=dff['Se considera']
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
tree.plot_tree(dtree, feature_names=cod_preguntas)
plt.figure()
plot_tree(dtree, filled=True)
plt.title("Diversidad Sexual según Edad")
#plt.show()
plt.savefig('tree.pdf')