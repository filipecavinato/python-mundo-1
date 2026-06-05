# Script criado por Filipe Cavinato

s = float(input('Digite seu salario: '))

if s > 1250.0:
    print('Novo salario, com {}% de aumento: R$ {:.2f}'.format(10, s + s*0.10))
else:
    print('Novo salario, com {}% de aumento: R$ {:.2f}'.format(15, s + s*0.15))
