sal = float(input('Qual é o salário do funcionário? '))

if sal > 1250:
    sal_atual= sal + (sal * 10/100)
    print(f'O salário atual é de R${sal_atual}')

else:
    sal_atual= sal + (sal * 15/100)
    print(f'O salário atual é de R${sal_atual}')