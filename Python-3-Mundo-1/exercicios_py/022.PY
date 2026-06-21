nome = input('Digite seu nome: ').title().strip()

print('Seu nome em maiúsculo é ', nome.upper())
print('Seu nome em minúsculo é ', nome.lower())
print('Seu nome tem ao todo ', len(nome) - nome.count(' '))
separa =nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {nome.find(' ')} letras')
