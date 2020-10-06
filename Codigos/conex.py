import pymongo as pym
import pandas as pd
import json
import urllib3

# url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
# http = urllib3.PoolManager()
# resp = http.request('GET', url)
# datos = resp.data.decode('UTF-8')

client = pym.MongoClient("mongodb://fandres21:felipe1997@cluster0-shard-00-00.eghxh.mongodb.net:27017,cluster0-shard-00-01.eghxh.mongodb.net:27017,cluster0-shard-00-02.eghxh.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-wjnr0i-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['covid']
collection = db['muertos']

def get_data():
	URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
	df = pd.read_csv(URL)
	df = df.rename(columns={"Region": "fecha"})
	df["fecha"] = pd.to_datetime(df["fecha"])
	df = df.set_index("fecha")
	df = df.sort_index()
	return df
#print(datos)
#data = {"text" : "hello"}
result = collection.insert_one(get_data())
print(result.inserted_id)
#print(client.list_database_names())