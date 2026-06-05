# Script criado por Filipe Cavinato

x = input('Digite algo: ')
print('O Tipo Primito desse valor é {}'.format(type(x)))
print('Só tem espaços ? {}'.format(x.isspace()))
print('É um número ? {} '.format(x.isnumeric()))
print('É Alfabético ? {}'.format(x.isalpha()))
print('É Alfanumérico ? {}'.format(x.isalnum()))
print('É todo em letras Maiúsculas ? {}'.format(x.isupper()))
print('É todo em letras Minusculas ? {}'.format(x.islower()))
print('Esta capitalizado ? {}'.format(x.istitle()))
