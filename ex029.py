# Script criado por Filipe Cavinato

v = float(input('Digite a velocidade do carro: '))

if v > 80:
    multa = 7.00*(v - 80)
    print('Você foi multado! Você excedeu o limite de 80 Km/h\nSua multa vai custar R$ {:.2f}'.format(multa))
else:
    print('Sua Velocidade é de {} Km/h. Você está dentro do limite!\nDirija com segurança'.format(v))
