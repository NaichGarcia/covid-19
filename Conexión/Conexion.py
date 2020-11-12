import pymongo as pm
from bson.json_util import loads, dumps
import os.path as path

class Database(object):
    URI="mongodb://root:FVo8Ujz3XAPxVLwn@cluster0-shard-00-00.eghxh.mongodb.net:27017,cluster0-shard-00-01.eghxh.mongodb.net:27017,cluster0-shard-00-02.eghxh.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-wjnr0i-shard-0&authSource=admin&retryWrites=true&w=majority"
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
        Insert=Database.DATABASE[collection].insert_one(data)
        return Insert.inserted_id

    #Obtener datos de Database
    @staticmethod
    def Get_Data_from_database(collection):
        bd = Database.DATABASE[collection]
        #Consulta limitada a 2 objetos
        datos=bd.find().limit(2)

        return datos

    @staticmethod
    def Bson_to_Json(datos,nameFile):
        json_str= dumps(datos)
        json_encode=json_str.encode(encoding='UTF-8',errors='strict')
        with open('../Templates/'+nameFile+'.json','wb') as f:
            f.write(json_encode)
        if path.exists('../Templates/'+nameFile+'.json'):
            return '{"statuscode" : 200,"File" : '+nameFile+'}'
        
    @staticmethod 
    def Query(collection,dato,rest): 
        bd = Database.DATABASE[collection] 
        myquery = {dato:rest} 
        result = bd.find(myquery) 
        return result