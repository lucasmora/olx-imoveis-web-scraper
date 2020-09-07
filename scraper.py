import requests
from bs4 import BeautifulSoup
import pandas as pd

# O site da OLX exige que cabeçalhos sejam enviados
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

n_paginas = 2

# Cada objeto Imóvel será armazenado nesta lista
imoveis = []

# Lendo a quantidade de páginas especificadas
for pagina in range(1, n_paginas + 1):
    print("Lendo página {}...".format(pagina))
    url = 'https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/imoveis/aluguel?o=' + str(pagina) + '&pe=10000&ps=1'
    documento = requests.get(url, headers=headers)
    sopa = BeautifulSoup(documento.content, 'html.parser')

    for i in sopa.find_all('a', {'class': 'fnmrjs-0'}):
        titulo = i.find('h2').text

        preco = i.find('span', 'hLiLwY').text

        vagas = 0
        quartos = 0
        tamanho = 0
        condominio = 0

        # TODO: Melhorar esse loop para contemplar também os dados que não têm o pipe (|).
        infos = i.findAll('span', 'sc-ifAKCX sc-1j5op1p-0 fDwtTK')
        for info in infos:
            if '|' in info.text:
                for t in info.text.split('|'):
                    # TODO: Cortar somente os números.
                    if 'quarto' in t:
                        quartos = t
                    elif 'vaga' in t:
                        vagas = t
                    elif 'm²' in t:
                        tamanho = t
                    elif 'Condomínio' in t:
                        condominio = t
            else:
                print(info)
                print('-' * 50)

        # Criando lista de atributos de cada imóvel
        imovel = [titulo, preco, condominio, quartos, tamanho, vagas]
        imoveis.append(imovel)

# Criando DataFrame com os dados de cada registro
df = pd.DataFrame(columns=['titulo', 'preco', 'condominio', 'quartos', 'tamanho', 'vagas'], data=imoveis)

# TODO: Formatar os tipos de dados de cada coluna.

print("\n{} páginas lidas.".format(n_paginas))
print("{} registros adicionados.\n".format(str(df.shape[0])))

# Salvando em CSV
df.to_csv("df.csv")
