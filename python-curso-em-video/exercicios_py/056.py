somaidade = 0 
maioridadeh= 0
nomevelho = ""
mulher20= 0

for i in range(1, 5):
    print(f"----- {i}° PESSOA -----")
    nome = input("Nome: ").strip().upper()
    idade = int(input("idade: "))
    sexo= input("Sexo [M/F]: ").strip().upper()
    somaidade += idade

    if i ==1 and sexo in "M" :
        maioridadeh = idade
        nomevelho= nome

    if sexo in "M" and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome

    if sexo in "F" and idade < 20:
        mulher20 += 1

media = somaidade / 4
print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {maioridadeh} anos e se chama {nomevelho}")
print(f"Ao todo são {mulher20} mulheres com menos de 20 anos")