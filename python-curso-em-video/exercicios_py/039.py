from datetime import date
atual = date.today().year

ano = int(input("Ano de nascimento: "))
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} anos em 2026")

if idade >=18:
    if idade == 18:
        print(f"Você tem que se alistar esse ano")

    else:
        diferenca = idade - 18
        alistamento =  atual - diferenca
        print(f"Você já deveria ter se alistado há {diferenca} ano(s)")
        print(f"Seu alistamento foi em {alistamento}")

else:
   diferenca = 18 - idade
   alistamento = atual + diferenca
   print(f"Aindam faltam {diferenca} anos para o alistamento")
   print(f"Seu alistaemnto será em {alistamento}")  