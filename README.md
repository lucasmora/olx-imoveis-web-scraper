# Web Scraper - Aluguéis particulares em Curitiba
Este web scraper tem como objetivo extrair informações de preço e descrições de imóveis para aluguel do site OLX.com.br. A pesquisa foi filtrada para a cidade de Curitiba, PR.
Os dados são exportados para um arquivo .CSV, a fim de facilitar a análise posterior.

## Bibliotecas e dependências
- Python 3.8
- BeautifulSoup 4.9.1 (com *requests 2.24*), para baixar as páginas do servidor
- RegEx, para filtrar os textos dos anúncios
- Pandas 1.1.1, para formatar e exportar os dados extraídos

## Atributos extraídos
Os atributos de cada imóvel foram deliberadamente selecionados:
- Título do anúncio
- Bairro
- Preço do aluguel
- Preço do condomínio, se aplicável
- Quantidade de quartos
- Tamanho do imóvel
- Vagas de garagem
- Link para o anúncio no website
