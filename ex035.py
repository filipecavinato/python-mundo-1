# Script criado por Filipe Cavinato

print('-=-' *10)
print('Analisador de Triangulos')
print('-=-' *10)

r1 = float(input('Digite o tamanho da 1º reta: '))
r2 = float(input('Digite o tamanho da 2º reta: '))
r3 = float(input('Digite o tamanho da 3º reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Os lados [{}, {}, {}] podem formar um triangulo!'.format(r1,r2,r3))
else:
    print('Os lados [{}, {}, {}] NÃO PODEM formar um triangulo!'.format(r1,r2,r3))
