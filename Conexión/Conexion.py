import pymongo as pm

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
    