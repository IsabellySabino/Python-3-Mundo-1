n = int(input("Digite um número: "))
opcao = int(input("Escolha uma opção:\n[1] Converter para BINÁRIO\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL\n"))

if opcao == 1:
    print("O número binário é ", bin(n))

elif opcao == 2:
    print("O número octal é ", oct(n))
    

elif opcao == 3:
    print("O número hexadecimal é ", hex(n))

else:
    print("Opção inválida. Tente novamente!")