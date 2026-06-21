from math import radians, sin, cos, tan
angulo = int(input('Digite o ângulo que você deseja: '))
seno= sin(radians(angulo))
co = cos(radians(angulo))
tan = tan(radians(angulo))

print(f'O ângulo {angulo} tem o seno {seno:.2f}\nO cosseno {co:.2f}\nE a tangente {tan:.2f} ')