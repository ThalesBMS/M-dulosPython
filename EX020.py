#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

grp1 = input('Digite o nome do primeito do aluno: ')
grp2 = input('Digite o nome do segundo do aluno: ')
grp3 = input('Digite o nome do terceito do aluno: ')
grp4 = input('Digite o nome do quarto do aluno: ')
lista = [grp1, grp2, grp3, grp4]
ordem = random.shuffle(lista)
print('A ordem é {}'.format(lista))