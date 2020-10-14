import pymongo as pm
from bson.json_util import loads, dumps


class Database(object):
    URI="mongodb://fandres21:felipe1997@cluster0-shard-00-00.eghxh.mongodb.net:27017,cluster0-shard-00-01.eghxh.mongodb.net:27017,cluster0-shard-00-02.eghxh.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-wjnr0i-shard-0&authSource=admin&retryWrites=true&w=majority"
    DATABASE=None

    #Inicializa la conexión hacia MongoDB
    @staticmethod
    def initialize(database):
        client=pm.MongoClient(Database.URI)
        Database.DATABASE=client[database]

    @staticmethod
    def getDatabase():
        client=pm.MongoClient(Database.URI)
        bd=client.list_database_names()
        return bd

    #Insertar Muchos datos (Registros) a MongoDB
    @staticmethod
    def InsetManyData(collection,data):
        Insert=Database.DATABASE[collection].insert_many(data)
        return Insert.inserted_ids
        

    #Insertar un dato (Registro) a MongoDB
    @staticmethod
    def InsetOneData(collection,data):
        Database.DATABASE[collection].insert_one(data)
    
    #Obtener datos de Database
    @staticmethod
    def Get_Data_from_database(collection):
        bd = Database.DATABASE[collection]
        datos=bd.find().limit(2)
        json_str =dumps(datos)
        datos2=loads(json_str)
        datos2=str(datos2)
        datos2=datos2.encode(encoding='UTF-8',errors='strict')
        with open('../Templates/template.json','w') as f:
            f.write(str(datos2))
        return datos2



