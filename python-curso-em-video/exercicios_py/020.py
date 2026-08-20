import random 

n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')

alunos= [n1, n2, n3, n4]

random.shuffle(alunos)
print('A ordem ', alunos)