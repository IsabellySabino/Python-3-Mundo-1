frase = input('Digite uma frase: ').upper().strip()
separa = frase.split()
print(f'A letra A aparece {frase.count('A')}\nA primera letra A aparece na posição {frase.find('A')+1}\nA última letra A apareceu na posição {frase.rfind('A')+1}')