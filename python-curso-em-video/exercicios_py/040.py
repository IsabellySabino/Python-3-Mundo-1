n1 = float(input("Insira sua nota: "))
n2 = float(input("Insira sua outra nota: "))

media = (n1 + n2) / 2

if media < 5:
    print(f"Tirando {n1} e {n2}, a média do aluno é {media}\nO aluno está REPROVADO")

elif media < 6.9:
     print(f"Tirando {n1} e {n2}, a média do aluno é {media}\nO aluno está de RECUPERAÇÃO")

else:
     print(f"Tirando {n1} e {n2}, a média do aluno é {media}\nO aluno está APROVADO")