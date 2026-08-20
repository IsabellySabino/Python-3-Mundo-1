velo = float(input('Qual a velociade atual do carro ? '))
8
if velo > 80:
    print(f'MULTA! Você excedeu a velocidade permitida que é de 80 km/h')
    multa= (velo - 80) * 7
    print(f'O valor da muta é de R${multa:.2f}')
else:
    print('Bom dia! Dirija com segurança!')