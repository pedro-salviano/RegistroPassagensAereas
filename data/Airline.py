'''
File: Airline.py
Project: data
Create Date: Sunday, 1st December 2024
----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''

from mongoengine import Document, StringField, IntField, ObjectIdField

class Airline(Document):
    razao_social = StringField(required = True)
    icao = StringField(required = False)
    iata = StringField(required = False)
    email = StringField(required = True)