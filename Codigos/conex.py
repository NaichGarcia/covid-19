import pymongo as pym
import pandas as pd


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



URL = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv"
df = pd.read_csv(URL)

df.reset_index(inplace=True)
data_dict = df.to_dict("records")
result=collection.insert_many(data_dict)
print(result.inserted_ids)
