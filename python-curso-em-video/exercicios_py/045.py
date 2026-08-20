from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

jogador = int(input("Suas opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nQual a sua jogada?"))

print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")

if computador == 0:
    if jogador ==0:
        print("EMPATE")

    elif jogador ==1:
        print("JOGADOR VENCE")

    elif jogador == 2:
        print("COMPUTADOR VENCE")

    else:
        print("JOGADA INVÁLIDA")

elif computador ==1:
    if jogador ==0:
         print("COMPUTADOR VENCE")
    
    elif jogador ==1:
        print("EMPATE")
    
    elif jogador == 2:
        print("JOGADOR VENCE")
    
    else:
        print("JOGADA INVÁLIDA")

else:
    if jogador ==0:
        print("JOGADOR VENCE")
    
    elif jogador ==1:
        print("COMPUTADOR VENCE")
    
    elif jogador == 2:
        print("EMPATE")
    
    else:
        print("JOGADA INVÁLIDA")
    


