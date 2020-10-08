from Conexion import Database as db
import pymongo as pym
import pandas as pd

#Inicializar nuestra conexión 
db.initialize('covid')

#Nombre de la colección a crear o usar
collection='muertos'

#Obtención de las bases de datos de mongo (SOLO PRUEBA)
databases=db.getDatabase()
print(databases)


#Obtención de datos por csv 
URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
df = pd.read_csv(URL)
df.reset_index(inplace=True)
data_dict = df.to_dict("records")

#Insert de datos 
result=db.InsetManyData(collection,data_dict)
#Imprime todas las ID creadas con respecto a los insert
#print(result)

z=db.Get_Data_from_database(collection)
print(z)