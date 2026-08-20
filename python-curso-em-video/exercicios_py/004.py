n = (input('Digite algo: '))

print(f'O tipo primitivo desse valor é {type(n)}')

print('Só te espaço?', n.isspace())

print('é um número?', n.isnumeric())

print('é alfabético?', n.isalpha())

print('é um alfanúmerico?', n.isalnum())

print(f'Está em letras maiúsculas?{n.isupper()}')

print(f'Está em letras minúsculas?{n.islower()}', )

print(f'Está capitalizado?{n.istitle()}')

