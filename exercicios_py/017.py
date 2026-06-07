from math import sqrt
c_oposto = float(input('Comprimento do cateto oposto: '))
c_adjacente= float(input('Comprimento do cateto oposto: '))

soma = c_oposto**2 + c_adjacente**2
h = sqrt(soma)

print(f'O cateto oposot vale {c_oposto} e o cateto adjacente {c_adjacente}, a soma dos catetos é {soma}, e a hipotenusa é {h}')