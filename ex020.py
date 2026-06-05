# Script criado por Filipe Cavinato

from random import shuffle

a1 = input('Digite o nome do 1º Aluno: ')
a2 = input('Digite o nome do 2º Aluno: ')
a3 = input('Digite o nome do 3º Aluno: ')
a4 = input('Digite o nome do 4º Aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)

print('Ordem de Apresentação:')
print('1º {}\n2º {}\n3º{}\n4º{}'.format(lista[0],lista[1],lista[2],lista[3]))
