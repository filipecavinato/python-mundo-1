# Script criado por Filipe Cavinato

cid = str(input('Digite o nome da sua cidade: ')).strip().capitalize()

if not ('Santo' in cid):
    print('A cidade não começa com "Santo"')
else:
    print('A cidade começa com "Santo"')
