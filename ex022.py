# Script criado por Filipe Cavinato

nome = str(input('Digite seu nome completo: ')).strip()
nome_div = nome.split()
print('Analisando seu nome:')
print('Maiusculas = {}'.format(nome.upper()))
print('Minusculas = {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome.replace(' ',''))))
print('Total de letras do Primeiro Nome: {}'.format(len(nome_div[0])))
