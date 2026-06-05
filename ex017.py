# Script criado por Filipe Cavinato

from math import pow, sqrt

c1 = float(input('Digite o valor do 1º Cateto: '))
c2 = float(input('Digite o valor do 2º Cateto: '))
h = sqrt(pow(c1,2) + pow(c2,2))

print('Um triangulo com catetos {:.2f} e {:.2f} tem hipotenusa igual a {:.2f}'.format(c1,c2,h))
