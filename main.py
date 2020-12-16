import argparse
import scraper_aluguel, scraper_venda

parser = argparse.ArgumentParser(description='Extrai informações de aluguel.')
parser.add_argument('-a', action='store_true', help='extrai dados de imóveis para aluguel')
parser.add_argument('-v', action='store_true', help='extrai dados de imóveis para venda')

args = parser.parse_args()

if args.a == False and args.v == False:
    scraper_aluguel.scraper_aluguel()
    scraper_venda.scraper_venda()
else:
    if args.a == True:
        scraper_aluguel.scraper_aluguel()

    if args.v == True:
        scraper_venda.scraper_venda()