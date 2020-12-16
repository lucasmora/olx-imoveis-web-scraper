# Web Scraper - Aluguéis e vendas particulares em Curitiba

Este web scraper tem como objetivo extrair informações de preço e descrições de imóveis (casas e apartamentos) para aluguel e venda do site [OLX](https://www.olx.com.br). A pesquisa foi filtrada para a cidade de Curitiba, PR.
Os dados são exportados para um arquivo .CSV, facilitando a análise posterior.

## Como usar

Para extrair __todas__ as informações, rodar sem nenhuma flag.

Para extrair apenas informações de __aluguéis__, rodar com a flag `-a`:  
`python main.py -a`

Para extrair apenas informações de __venda__, rodar com a flag `-v`:
`python main.py -v`


## Bibliotecas e dependências

- Python 3
- BeautifulSoup 4.9.3 com *requests 2.2* e *lxml*
- RegEx
- Pandas 1.1.4

## Atributos extraídos

Os atributos de cada imóvel foram deliberadamente selecionados:

- Título do anúncio
- Bairro
- Preço do aluguel
- Preço do condomínio
- Quantidade de quartos
- Tamanho do imóvel
- Vagas de garagem
- Link para o anúncio no website
