#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n1 = float(input('Digite um numero: '))
print('A parte inteira do número {} é: {}'.format(n1,math.trunc(n1)))
