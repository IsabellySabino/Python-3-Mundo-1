n = int(input("Digite um número: "))
tot = 0

for i in range(1, n+1):
    if n % i == 0:
        print("\033[33m", end=" ")
        tot += 1

    else:
        print("\033[31m", end=" ")

    print(f"{i}", end="")
print(f"\nO número {n} foi divisível {tot} vezes")
if tot ==2:
    print("E por isso ele é PRIMO")

else:
    print("E por isso ele NÃO É PRIMO")