# Script criado por Filipe Cavinato

from random import randint

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar..')
print('-=-' * 20)
n = randint(1,5)
esc = int(input('Qual número eu estou pensando: '))

if esc == n:
    print('Parabens, você ganhou, pensei no número {}'.format(n))
else:
    print('Você perdeu! Eu pensei no número {}'.format(n))
