# Web Scraper - Aluguéis particulares em Curitiba

Este web scraper tem como objetivo extrair informações de preço e descrições de imóveis para aluguel do site [OLX](https://www.olx.com.br). A pesquisa foi filtrada para a cidade de Curitiba, PR.
Os dados são exportados para um arquivo .CSV, facilitando a análise posterior.

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
