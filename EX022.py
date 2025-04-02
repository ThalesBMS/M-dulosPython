nome = str(input('Digite seu nome completo: ')).strip() #Tirar espaços antes e depois
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
sep = (nome.split())
print('Seu primeiro nome é {} e ele tem {} letras'.format(sep [0], len(sep[0])))