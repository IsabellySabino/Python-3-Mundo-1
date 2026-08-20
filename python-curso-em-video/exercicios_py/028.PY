from random import randint
from time import sleep

numero = randint(0,5)

n= int(input('NÚMERO SORTEADO\nQual foi o número escolhido pelo computador?Entre 0 à 5 '))
print('PROCESSANDO')
sleep(3)

if n == numero:
    print(f'PARABÉNS, VOCÊ VENCEU!\nO número é {numero}')

else:
    print(f'VOCÊ PERDEU!\nO numero era {numero}')