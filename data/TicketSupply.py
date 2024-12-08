'''
File] = TicketSupply.py
Project] = data
Create Date] = Sunday, 1st December 2024
----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField, BooleanField


class Airplane(EmbeddedDocument):
    modelo = StringField(required = True)
    matricula = StringField(min_length=5, max_length=8, required= True)

class Details(EmbeddedDocument):
    janela= BooleanField(required=False)
    aeronave = EmbeddedDocumentField(Airplane, required= False)

class TicketSupply(Document):
    ano = IntField(required=True)
    mes = IntField(required=True)
    dia = IntField(required=True)
    empresa = StringField(required=True)
    icao_origem = StringField(required=True)
    icao_destino = StringField(required=True)
    tarifa = StringField(required=True)
    tickets = IntField(required=True, min_value=0)

    caracteristicas= EmbeddedDocumentField(Details, required= False)

    meta = {
        'db_alias': 'default',
        'auto_create_index': True,
        'auto_create_index_on_save': True,
        'indexes':[
            {
                'fields':[('$icao_origem', '$icao_destino'), 'ano', 'mes', 'dia']
            }
        ]
    }

    @classmethod
    def findSupply(cls, icao_origem='', icao_destino='', dia='', mes='', ano=''):
        filter = {}
        if(icao_origem != ''):
            filter['icao_origem'] = icao_origem
        
        if(icao_destino != ''):
            filter['icao_destino'] = icao_destino

        if(dia != ''):
            filter['dia'] = int(dia)
        
        if(mes != ''):
            filter['mes'] = int(mes)

        if(ano != ''):
            filter['ano'] = int(ano)

        return cls.objects(__raw__ = filter)