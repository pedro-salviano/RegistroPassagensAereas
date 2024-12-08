# RegistroPassagensAereas
Repositório para desenvolvimento do Trabalho 1, da disciplina de bancos de dados para ciência de dados, ofertada pela Profa. Dra. Marcela Xavier Ribeiro, no período 2024/2

## Aplicação para vendas de passagens aéreas
Trabalho 1 de Banco de Dados para Ciência de Dados
Pedro Augusto Benevides Salviano - 790983

## Aplicação
O presente trabalho objetiva apresentar uma aplicação para registro de ofertas de passagens aéreas, no qual pode ser feito o cadastro de passagens para venda, informando ano, mês e data da viagem, origem, destino, o valor da tarifa e quantidade de passagens disponíveis e a aquisição de uma quantidade igual ou inferior de  passagens pelo valor ofertado.
	A aplicação terá interação via CLI, e só contará com recursos de cadastrar ofertas de passagens, ou adquirir passagens.
	Os dados iniciais cadastrados foram extraídos do sistema SAS (https://sas.anac.gov.br/sas/downloads/view/frmDownload.aspx) e do sistema de dados abertos (https://sistemas.anac.gov.br/dadosabertos/), ambos  da ANAC, sendo os temas:
Tarifas Transporte Aéreo Passageiros Domésticos (Acessado em 30/11/2024);
Acessível no SAS, foi feito o download de todos conjuntos do ano de 2023 e agregados em um único documento para ser importado no mongoDB
Empresas Aéreas Outorgadas (Acessado em 30/11/2024);
Acessível no SAS, foi feito o download apenas do conjunto 20231225.CSV
Lista de aeródromos públicos (Acessado em 30/11/2024); (https://sistemas.anac.gov.br/dadosabertos/Aerodromos/Aer%C3%B3dromos%20P%C3%BAblicos/Lista%20de%20aer%C3%B3dromos%20p%C3%BAblicos/AerodromosPublicos.csv)
Disponível no sistema de dados abertos no caminho “Aerodromos/Aeródromos Públicos/Lista de aeródromos públicos/AerodromosPublicos.csv”

## Importação Dados
Os dados originais podem ser acessados nas respectivas fontes listadas na seção de aplicação, porém também foram disponibilizados no repositório do github (https://github.com/pedro-salviano/RegistroPassagensAereas/tree/main/Dados/OriginalData). Os dados originais passaram por processamento, sendo que os conjuntos de Tarifas Transporte Aéreo Passageiros Domésticos foram agregados em um único csv utilizando a ferramenta https://mightymerge.io/merge-csv-files/, as colunas de todos os conjuntos foram renomeadas, e os dados já processados podem ser acessados zipados em https://github.com/pedro-salviano/RegistroPassagensAereas/blob/main/Dados/DadosInsercao.zip. Após inseridos, os dados de tarifas precisaram receber um dia, uma vez que o conjunto original inclui apenas as informações das diferentes tarifas aplicadas em cada mês, para tal o script https://github.com/pedro-salviano/RegistroPassagensAereas/blob/main/Dados/mongoscripts/insertRandomDayInfo foi utilizado. 

## Vídeo Pitch
	https://drive.google.com/file/d/1zVuX2xA6rC_7O3f6dHrrlnJkdCOmXI4y/view?usp=drive_link 

## Referências
MongoEngine User Guide: https://docs.mongoengine.org/guide/ 
Dados Abertos ANAC: https://sistemas.anac.gov.br/dadosabertos/
SAS ANAC: https://sas.anac.gov.br/sas/downloads/view/frmDownload.aspx
