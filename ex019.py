# Script criado por Filipe Cavinato

from random import choice

a1 = input('Digite o nome do 1º Aluno: ')
a2 = input('Digite o nome do 2º Aluno: ')
a3 = input('Digite o nome do 3º Aluno: ')
a4 = input('Digite o nome do 4º Aluno: ')
lista = [a1, a2, a3, a4]
sort = choice(lista)

print('O aluno escolhido foi {}'.format(sort))
