#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite um angulo para saber seu seno, cos e tan: '))
seno = math.sin(math.radians(ang))
print('O angulo {} tem o seno de valor {:.2f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O angulo {} tem o coseno de valor {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O angulo {} tem a tangente de valor {:.2f}'.format(ang, tan))