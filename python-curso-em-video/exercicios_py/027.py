nome = input('Digite seu nome completo: ').title().strip()
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}\nSeu último nome é {separa[len(separa)-1]}')