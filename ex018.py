# Script criado por Filipe Cavinato

from math import sin, cos, tan, radians

a = float(input('Digite um angulo: '))

print('Seno {}º = {:.2f}\nCos {}º = {:.2f}\nTan {}º = {:.2f}'.format(a,sin(radians(a)),a,cos(radians(a)),a,tan(radians(a))))
