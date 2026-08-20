v_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int (input("Quantos anos você vai pagar a casa? "))

prestacao = v_casa / (anos /12)

if prestacao > (salario + salario * 0.30):
    print("O empréstimo foi negado!\nO valor da prestação ultrassa 30% do seu salário")

else:
    print("O empréstimo foi aprovado!")