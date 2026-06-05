# Script criado por Filipe Cavinato

l = float(input('Digite a Largura (em metros): '))
h = float(input('Digite a Altura (em Metros): '))

print('Para pintar uma Parede de {:.2f} x {:.2f} ({} m²)\nVocê precisará de {:.2f} Litros de tinta'.format(l,h,l*h,(l*h/2)))
