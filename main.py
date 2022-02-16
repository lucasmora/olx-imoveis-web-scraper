import sys
import argparse
import scraper_aluguel, scraper_venda

parser = argparse.ArgumentParser(description='Extrai informações de aluguel e venda do site OLX.com.br.')
parser.add_argument('-a', action='store_true', help='extrai dados de imóveis para aluguel')
parser.add_argument('-v', action='store_true', help='extrai dados de imóveis para venda')
parser.add_argument('-p', action='append', metavar='X', help='extrai X páginas')

args = parser.parse_args()

if args.p is not None:
    paginas = int(args.p[0])
else:
    paginas = 2

if args.a == False and args.v == False:
    scraper_aluguel.scraper_aluguel(paginas)
    scraper_venda.scraper_venda(paginas)
else:
    if args.a == True:
        scraper_aluguel.scraper_aluguel(paginas)

    if args.v == True:
        scraper_venda.scraper_venda(paginas)