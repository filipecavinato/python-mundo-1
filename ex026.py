# Script criado por Filipe Cavinato

f = str(input('Digite uma frase: ')).strip().upper()

print('A Letra "A" aparece {} vezes na frase'.format(f.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(f.find('A')+1))
print('A ultima letra "A" apareceu na posição {}'.format(f.rfind('A')+1))
