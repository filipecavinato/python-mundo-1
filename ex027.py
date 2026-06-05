# Script criado por Filipe Cavinato

n = str(input('Digite seu nome completo: ')).strip().title()
n_div = n.split()

print('Muito prazer em te conhecer, {}!'.format(n))
print('Seu primeiro nome é {}'.format(n_div[0]))
print('Seu ultimo nome é {}'.format(n_div[len(n_div) - 1]))
