frase = input("Digite uma frase: ").upper()
texto = frase.replace(" ", "")
reverso = ""



for caractere in reversed(texto):
    reverso += caractere

print(f"O inverso de {texto} é {reverso}")

if texto == reverso:
    print("Temos um palíndromo")


else:
    print("A frase digitada não é um palíndromo!")
