from datetime import date
ano = date.today().year

nasc= int(input("Ano de nasciemnto: "))
idade = ano - nasc
print(f"O atleta tem {idade} ano(s)")

if idade <= 9:
    print("Classificação: MIRIM")

elif idade <= 14:
    print("Classificação: INFANTIL")

elif idade <= 19:
    print("Classificação: JÚNIOR")

elif idade <= 25:
    print("Classificação: SÊNIOR")

else:
    print("Classificação: MASTER")