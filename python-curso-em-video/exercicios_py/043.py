peso = float(input("Qual o seu peso? (Kg)"))
altura =  float(input("Qual é a sua altura? (M)"))

imc = peso / (altura * altura)
print(f"O IMC dessa pessoa é de {imc:.2f}")

if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")

elif imc < 25:
    print("Você está com o PESO IDEAL")

elif imc < 30:
    print("Você está com o SOBREPESO")

elif imc < 40:
    print("Você está com Obesidade")

else:
    print("Você está com Obesidade Mórbida")