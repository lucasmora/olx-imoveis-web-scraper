import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scraper_aluguel():
    # O site da OLX exige que cabeçalhos sejam enviados
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    # Número de páginas a serem lidas
    n_paginas = 2

    # As informações de cada imóvel serão armazenadas nesta lista
    imoveis = []

    # Lendo a quantidade de páginas especificadas
    for pagina in range(1, n_paginas + 1):
        print("Extraindo página {}...".format(pagina))
        url = 'https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/imoveis/aluguel?o=' + str(pagina) + '&pe=10000&ps=1'
        documento = requests.get(url, headers=headers)
        sopa = BeautifulSoup(documento.content, 'html.parser')

        padrao = "([0-9.]+)"  # Padrão RegEx para extrair números com e sem pontos decimais

        for i in sopa.find_all('a', {'class': 'fnmrjs-0'}):
            link = i.parent.findAll('a')[0].get_attribute_list('href')[0]  # Link do anúncio

            titulo = i.find('h2').text  # Título do anúncio

            # Extraindo e formatando o preço
            preco = i.find('span', 'eoKYee').text
            preco = re.search(padrao, preco).group()
            preco = preco.replace(".", "")

            # Inicializando variáveis
            vagas = 0
            quartos = 0
            tamanho = 0
            condominio = 0
            bairro = ''
            bairro = i.find('span', 'dpURtf').text

            # Encontrando e dividindo as informações sobre condomínio, quartos, tamanho e vagas de garagem
            infos = i.find('span', 'eLPYJb')
            for info in infos:
                if '|' in info:
                    for t in info.split('|'):
                        if 'quarto' in t:
                            quartos = re.search(padrao, t).group()
                        elif 'vaga' in t:
                            vagas = re.search(padrao, t).group()
                        elif 'm²' in t:
                            tamanho = re.search(padrao, t).group()
                        elif 'Condomínio' in t:
                            condominio = re.search(padrao, t).group()
                else:
                    if 'quarto' in info:
                        quartos = re.search(padrao, info).group()
                    elif 'vaga' in info:
                        vagas = re.search(padrao, info).group()
                    elif 'm²' in info:
                        tamanho = re.search(padrao, info).group()
                    elif 'Condomínio' in info:
                        condominio = re.search(padrao, info).group()

                if condominio != 0:
                    condominio = condominio.replace(".", "")  # Removendo o ponto decimal para converter para int

            # Adicionando o imóvel recém criado à lista de imóveis
            imovel = [titulo, bairro, preco, condominio, quartos, tamanho, vagas, link]
            imoveis.append(imovel)

    # Criando DataFrame com os dados de cada registro
    df = pd.DataFrame(columns=['titulo', 'bairro', 'preco', 'condominio', 'quartos', 'tamanho', 'vagas', 'link'],
                    data=imoveis)

    # Formatando os tipos de dados corretos de cada coluna
    df['preco'] = df['preco'].astype('int')
    df['condominio'] = df['condominio'].astype('int')
    df['quartos'] = df['quartos'].astype('int')
    df['tamanho'] = df['tamanho'].astype('int')
    df['vagas'] = df['vagas'].astype('int')

    print("\n{} páginas extraídas. {} registros criados.\n".format(n_paginas, str(df.shape[0])))

    # Exportando para CSV
    arquivo = "imoveis.csv"
    df.to_csv(arquivo, encoding="utf-8", index=False, sep=';')
    print("Dados salvos como {}.".format(arquivo))