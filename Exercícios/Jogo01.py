#jogo de pedra papel e tesoura.
from random import randint
print('=-='*20)
print('Vamos jogar jokempô')
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada ? '))
print('=-='*20)
print('o computador JOGOU {}'.format(itens[computador]))
print('o jogador JOGOU {}'.format(itens[jogador]))
print('=-='*20)
if computador ==0: #computador jogou pedra
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print ('JOGADOR VENCEU')
    elif jogador ==2:
        print ('COMPUTADOR VENCEU')
    else: print('Jogada invalida')
elif computador ==1: #computador jogou papel
    if jogador ==0:
        print ('COMPUTADOR VENCEU')
    elif jogador ==1:
        print ('EMPATE')
    elif jogador ==2:
        print ('JOGADOR VENCEU')
    else: print ('Jogada invalida')
elif computador ==2: #computador jogou tesoura
    if jogador ==0:
        print ('JOGADOR VENCEU')
    elif jogador ==1:
        print ('COMPUTADOR VENCEU')
    elif jogador ==2:
        print ('EMPATE')
    else: print ('Jogada infvalida')