'''
File: ticketManagement.py
Project: RegistroPassagensAereas
Create Date: Sunday, 1st December 2024
----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''

"http://docs.mongoengine.org/index.htm"

from repository.databaseManager import MongoEngineManager
from data.Airport import Airport
from data.Airline import Airline
from data.TicketSupply import TicketSupply
from mongoengine.queryset.visitor import Q
from pprint import PrettyPrinter
import datetime
import calendar
import re
import json

def find():
    year = input("Ano: ")
    month = input("Mês: ")
    day = input("Dia: ")

    with MongoEngineManager() as db:
        origin_airport_query = input("Aeroporto de origem: ")
        origin_airports = Airport.objects.search_text(origin_airport_query)

        for airport in origin_airports:
            print('\n')
            pp.pprint(json.loads(airport.to_json()))
        icao_origem = input("Informe o cod ICAO do aeroporto de origem: ").upper()

        destination_airport_query = input ("Aeroporto de destino: ")
        destination_airports = Airport.objects.search_text(destination_airport_query)

        for airport in destination_airports:
            print('\n')
            pp.pprint(json.loads(airport.to_json()))
        icao_destino = input("Informe o cod ICAO do aeroporto de destino: ").upper()

        ticketSupply = TicketSupply.findSupply(icao_origem=icao_origem, icao_destino=icao_destino, dia=day, mes=month, ano=year)

        print("Ofertas encontradas:")
        for ticket in ticketSupply:
            print('\n')
            pp.pprint(json.loads(ticket.to_json()))
    
    return icao_origem, icao_destino, day, month, year

def offer():
    empresa: Airline
    aeroporto_origem: Airport 
    aeroporto_destino: Airport
    tarifa: str
    tickets: int
    data = datetime.date

    data = datetime.date(year = 1, month= 1, day = 1)

    with MongoEngineManager() as db:
    
        icao_empresa = input("Informe o ICAO da empresa: ").upper()

        empresa = Airline.objects(icao=icao_empresa).first()

        while(empresa is None):
            icao_empresa = input("ICAO empresa não encontrado tente novamente: ").upper()

            empresa = Airline.objects(icao=icao_empresa).first()
        
        print(f'Empresa selecionada: {empresa.razao_social}')

        icao_origem = input("Informe o ICAO do aeroporto de origem: ").upper()
        aeroporto_origem = Airport.objects(icao= icao_origem).first()

        while(aeroporto_origem is None):
            icao_origem = input("ICAO origem não encontrado tente novamente: ").upper()

            aeroporto_origem = Airport.objects(icao= icao_origem).first()

        print(f'Aeroporto origem selecionado: {aeroporto_origem.nome}')


        icao_destino = input("Informe o ICAO do aeroporto de destino: ").upper()
        aeroporto_destino = Airport.objects(icao= icao_destino).first()

        while(aeroporto_destino is None):
            icao_destino = input("ICAO destino não encontrado tente novamente: ").upper()

            aeroporto_destino = Airport.objects(icao= icao_destino).first()

        print(f'Aeroporto origem selecionado: {aeroporto_destino.nome}')

        tickets_input = input("Informe a quantidade de passagens ofertadas: ")
        while(not tickets_input.isdigit() or int(tickets_input) < 1):
            tickets_input = input("Quantidade inválida tente novamente: ")
        
        tickets = int(tickets_input)

        ano_input = input("Informe o ano da viagem: ")
        while(not ano_input.isdigit() or int(ano_input)< 2023 or int(ano_input)> 2027):
            ano_input = input("Ano inválido, tente novamente: ")

        data = data.replace(year = int(ano_input))

        mes_input = input("Informe o mês da viagem: ")
        while(not mes_input.isdigit() or int(mes_input)< 1 or int(mes_input)> 12):
            mes_input = input("Mês inválido, tente novamente: ")

        data = data.replace(month = int(mes_input))

        dia_input = input("Informe o dia da viagem: ")
        while(not dia_input.isdigit() or int(dia_input)< 1 or int(dia_input)> calendar.monthrange(data.year, data.month)[1]):
            dia_input = input("Dia inválido, tente novamente: ")

        data = data.replace(day = int(dia_input))

        tarifa = input("Informe o valor da tarifa por passagem, com até 2 casas decimais após a vírgula: ")
        while(not re.fullmatch("\d+,?\d{2}", tarifa)):
            tarifa = input("Tarifa inválida, tente novamente: ")

        tarifa_partes = tarifa.split(',')
        tarifa = tarifa if (len(tarifa_partes) == 2) else tarifa + ',00'
        

        passagens: TicketSupply = TicketSupply(
            empresa = empresa.icao,
            icao_origem= aeroporto_origem.icao,
            icao_destino = aeroporto_destino.icao,
            tickets = tickets,
            dia = data.day,
            mes = data.month,
            ano = data.year,
            tarifa = tarifa
        )

        print("Confirme a criação da oferta de passagens [(s) confirma; (m) modificar; (outra tecla) sair] :\n\n")
        pp.pprint(json.loads(passagens.to_json()))

        match input().lower():
            case "s":
                passagens.save()
                print("Oferta criada com sucesso!\n")
            case "m":
                offer()
            case _:
                return

def consume():
    (icao_origem, icao_destino, dia, mes, ano) = find()
    houveRefinamento:bool = False

    while(not icao_origem.isalpha()):
       houveRefinamento = True
       icao_origem = input("Informe o ICAO do aeroporto de origem: ").upper()

    while(not icao_destino.isalpha()):
       houveRefinamento = True
       icao_destino = input("Informe o ICAO do aeroporto de destino: ").upper()

    while(not ano.isdigit() or int(ano)< 2023 or int(ano)> 2027):
        houveRefinamento = True
        ano = input("Informe um ano válido: ")

    ano = int(ano)

    while(not mes.isdigit() or int(mes)< 1 or int(mes)> 12):
        houveRefinamento = True
        mes = input("Informe um mês válido: ")

    mes = int(mes)

    while(not dia.isdigit() or int(dia)< 1 or int(dia)> calendar.monthrange(ano, mes)[1]):
        houveRefinamento = True
        dia = input("Informe um dia válido: ")

    dia = int(dia)

    with MongoEngineManager() as db:
        tickets = TicketSupply.findSupply(icao_origem=icao_origem, icao_destino=icao_destino, dia=dia, mes=mes, ano=ano)

    if(houveRefinamento):
        print("Ofertas encontradas após refinamento:")
        for ticket in tickets:
            print('\n')
            pp.pprint(json.loads(ticket.to_json()))
    
    if(len(tickets) == 0):
        print("Nenhuma passagem encontrada!!")
        return

    tarifa = input("Qual a tarifa que você deseja adquirir? ")
    tarifa_partes = tarifa.split(',')
    tarifa = tarifa if (len(tarifa_partes) == 2) else tarifa + ',00'
    while(not re.fullmatch("\d+,?\d{2}", tarifa) or len(tickets.filter(tarifa = tarifa)) == 0):
        tarifa = input("Tarifa inválida, tente novamente: ")
        tarifa_partes = tarifa.split(',')
        tarifa = tarifa if (len(tarifa_partes) == 2) else tarifa + ',00'

    tickets = tickets.filter(tarifa = tarifa)

    tickets_input = input("Informe a quantidade de passagens desejadas: ")
    while(not tickets_input.isdigit() or int(tickets_input) < 1 or len(tickets(tickets__gte = int(tickets_input))) == 0):
        tickets_input = input("Quantidade inválida tente novamente: ")
    
    tickets_input = int(tickets_input)
    tickets = tickets(tickets__gte = tickets_input)

    ticket_selecionado:TicketSupply = tickets.first()

    aquisicao = json.loads(ticket_selecionado.to_json())

    aquisicao['tickets'] = tickets_input

    print("Confirme a aquisição da oferta de passagem [(s) confirma; (m) modificar; (outra tecla) sair] :\n\n")
    pp.pprint(json.loads(aquisicao))

    match input().lower():
        case "s":
            ticket_selecionado.tickets -= tickets_input
            with MongoEngineManager() as db:
                if(ticket_selecionado.tickets == 0):
                    ticket_selecionado.delete()
                else:
                    ticket_selecionado.save()
            print("Aquisição realizada com sucesso!\n")
        case "m":
            consume()
        case _:
            return


    
        

def main():
    while(True):
        op = input(
            '''
            Boas vindas ao ticketSupply!
            Selecione a operação desejada:
            1 - Procurar passagens
            2 - Ofertar passagens
            3 - Consumir passagens
            0 - Sair\n\n'''
        )

        match op:
            case '1':
                find()
            case '2':
                offer()
            case '3':
                consume()
            case '0':
                break
            case _:
                print('\nOperação não conhecida, tente novamente\n')

if __name__ == '__main__':
    pp = PrettyPrinter()
    main()

