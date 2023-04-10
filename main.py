import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scraper_aluguel(paginas):
    # O site da OLX exige que cabeçalhos sejam enviados
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    # Número de páginas a serem lidas
    n_paginas = paginas

    # As informações de cada imóvel serão armazenadas nesta lista
    imoveis = []

    print("Extraindo dados de aluguéis...")

    # Lendo a quantidade de páginas especificadas
    for pagina in range(1, n_paginas + 1) :
        url = 'https://www.olx.com.br/imoveis/aluguel/estado-se/sergipe/aracaju?o=2' + str(pagina) + '&pe=10000&ps=1'
        documento = requests.get(url, headers=headers)
        sopa = BeautifulSoup(documento.content, 'html.parser')

        for anuncio in sopa.find(id='ad-list'):
            try:
                link = anuncio.findAll('a')[0].get_attribute_list('href')[0]  # Link do anúncio

                titulo = anuncio.find('h2').text  # Título do anúncio

            # Extraindo e formatando o preço
                preco = anuncio.find('span', 'main-price').text
                preco = re.sub(r'[^\d,]', '', preco)
            except:
                link = 'false'
                titulo = 'false'
                preco = 'false'
            
            print(link, titulo, preco)
            imoveis.append([link, titulo, preco])
            df = pd.DataFrame(columns=['link', 'titulo', 'preco'],
                    data=imoveis)

            df.to_csv('imoveis_aluguel.csv', index=False)
            print("\n{} páginas extraídas. {} registros criados.\n".format(n_paginas, str(df.shape[0])))

    