import pandas as pd
import certifi
from pymongo.mongo_client import MongoClient
import json




class Mongodb_operation: 
    def __init__(self, client_uri: str, database_name: str, collection_name: str): 
        self.client_uri= client_uri
        self.database_name= database_name
        self.collection_name= collection_name

    def create_client(self): 
        ca = certifi.where()
        client=MongoClient(self.client_uri, tlsCAFile=ca)
        return client
    
    def create_database(self): 
        client=self.create_client()
        db=client[self.database_name]
        return db

    def create_collection(self, collection=None):
        database=self.create_database()
        collection=database[collection]
        return collection
        

    def insertone_data(self, record: dict, collection_name: str): 
        if type(record)== list: 
            for data in record: 
                if type(data) != dict: 
                    raise TypeError("Data must be form dict")
            collection=self.create_collection(collection_name)
            collection.insert_many(record)
        elif type(record)== dict: 
            collection=self.create_collection(collection_name)
            collection.insert_one(record)
    
    def bulk_data(self, datafile: str, collection_name: str=None): 
        self.path=datafile

        if self.path.endswith('.csv'): 
            data=pd.read_csv(self.path, encoding='utf-8')
        
        elif self.path.endswith('.xlsx'): 
            data=pd.read_excel(self.path, encoding='utf-8')
        
        json_data=json.loads(data.to_json(orient='records'))
        collection=self.create_collection(collection_name)
        collection.insert_many(json_data)
        



        