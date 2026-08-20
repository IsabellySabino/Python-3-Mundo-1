dis = float(input('Qual a distância da sua viagem? '))

if dis <= 200:
    preço= 0.50 * dis
    print(f'Você está preste a começar uma viagem de {dis}km/h\nE o preço da sua passagem será de {preço}')

else:
    preço= 0.45 * dis
    print(f'Você está preste a começar uma viagem de {dis}km/h\nE o preço da sua passagem será de {preço:.2f}')