# Script criado por Filipe Cavinato

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3:
    print('Maior: {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('Maior: {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('Maior: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('Menor: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('Menor: {}'.format(n2))
elif n3 < n1 and n3 < n2:
    print('Menor: {}'.format(n3))
