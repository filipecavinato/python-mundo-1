# Script criado por Filipe Cavinato
import datetime
from os import system

ano = int(input('Digite um ano (0 para o ano atual): '))
if ano == 0:
    ano_str = str(datetime.date.today().year)
else:
    ano_str = str(ano)

if ano == 0:
    ano = datetime.date.today().year

if ano_str[2:4] == '00':
    if ano % 4 == 0 and ano % 400 == 0:
        print('O ano {} É BISSEXTO!'.format(ano))
    else:
        print('O Ano {} NÃO É BISSEXTO!'.format(ano))
else:
    if ano % 4 == 0:
        print('O ano {} É BISSEXTO!'.format(ano))
    else:
        print('O Ano {} NÃO É BISSEXTO!'.format(ano))
