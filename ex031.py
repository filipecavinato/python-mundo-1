# Script criado por Filipe Cavinato

d = float(input('Qual a distancia da viagem (em Km): '))

if d <= 200:
    p = 0.5*d
else:
    p = 0.45*d

print('O valor da passagem para uma viagem de {} Km é de R$ {:.2f}'.format(d,p))
