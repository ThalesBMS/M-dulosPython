#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

co = float(input('Digite um valor para ser o cateto oposto de um triangulo retangulo: '))
ca = float(input('Digite outro valor para ser o cateto adjacente de um triangulo: '))
print('A hipotenusa do triangulo que tem seus catetos {} e {} é: {} '.format(co, ca, (ca**2 + co**2)**0.5))

#import math
#hi = math.hypot(co, ca)

