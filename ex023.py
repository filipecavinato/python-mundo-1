# Script criado por Filipe Cavinato

n = str(input('Digite um número entre 0 e 9999: '))

print('Unidade: {}'.format(n.rjust(4,'0')[3]))
print('Dezena: {}'.format(n.rjust(4,'0')[2]))
print('Centena: {}'.format(n.rjust(4,'0')[1]))
print('Milhar: {}'.format(n.rjust(4,'0')[0]))
