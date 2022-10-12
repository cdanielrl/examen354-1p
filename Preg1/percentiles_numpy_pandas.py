import numpy as np
import pandas as pd

preguntas=["Edad actual","Edad cuando sintió gusto o atracción física por primera vez por una persona","Edad tenía cuando tuvo su primer encuentro con alguien donde haya habido besos o caricias, y que usted estuviera de acuerdo","Edad de su primera relación sexual","Edad en que se dio cuenta de su orientación sexual"]
columnas=[1,55,56,60,74]
percentiles=[25,90,95]

df=pd.read_csv("..\\csv\\conjunto_de_datos_tmodulo_endiseg_web_2022.csv")

for i in range(len(preguntas)):
    datos=df.iloc[:,columnas[i]]
    resp=np.percentile(datos,percentiles)
    print("Primer cuartil "+preguntas[i]+" : "+str(resp[0]))
    print("Percentil 90 "+preguntas[i]+" : "+str(resp[1]))
    print("Percentil 95 "+preguntas[i]+" : "+str(resp[2]))