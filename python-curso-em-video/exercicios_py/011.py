preço = float(input('Digite o preço do produto: '))

desconto = preço*(5/100)
p_f = preço - desconto

print(f'O preço do produto é R${preço}, o valor do desconto é {desconto}, o preço atual é {p_f}')