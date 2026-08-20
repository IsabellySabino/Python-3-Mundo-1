km = float(input('Qual a quantidade de km rodado? '))
dia= int(input('Quantos dias o carro foi alugado? '))

valor = (dia * 60) + (km * 0.15)

print(f'O valor à pagar é R${valor}')