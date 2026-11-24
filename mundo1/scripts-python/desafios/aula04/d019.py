from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4] #Lista em Python fica entre colchetes
ar = choice(lista) # Choice recebe apenas um argumento
print(f'O aluno escolhido foi {ar}')