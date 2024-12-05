'''
File: databaseManager.py
Project: repository
Create Date: Sunday, 1st December 2024
----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''

from mongoengine import Document, StringField, IntField, connect, disconnect

class MongoEngineManager:
    def __init__(self, dbName= "Trabalho1_PassagensAereas", host = "localhost", port = 27017):
        self.dbName = dbName
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = connect(db = self.dbName, alias= 'default', host= self.host, port= self.port)
        except Exception as e:
            print(e)
    
    def disconnect(self):
        try:
            disconnect(alias= self.dbName)
        except Exception as e:
            print(e)
    
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()