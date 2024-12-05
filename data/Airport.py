'''
File: Airport.py
Project: data
Create Date: Sunday, 1st December 2024
----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''

from mongoengine import Document, StringField, FloatField
from mongoengine.queryset.visitor import Q

class Airport(Document):
    icao = StringField(required=False)
    ciad = StringField(required=False)
    nome = StringField(required=True)
    municipio = StringField(required=True)
    uf = StringField(required=True)
    municipio_servido = StringField(required=True)
    uf_servido = StringField(required=True)
    latgeopoint = FloatField()
    longeopoint = FloatField()
    latitude = StringField()
    longitude = StringField()
    altitude = StringField()

    meta = {
        'db_alias': 'default', 
        'indexes': [
            {
                'fields': ['$icao', "$ciad", "$nome", "$municipio", "$municipio_servido"],
                'default_language': 'portuguese',
                'weights': {'icao': 10, 'ciad': 10, 'nome': 5, 'municipio': 2, 'municipio_servido': 8}
            }
        ]
    }