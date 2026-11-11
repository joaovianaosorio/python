n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
# Você pode usar uma variável para a soma também
# Mas você pode criar a variável somente se você for usar a variável depois, esse não é o caso
print(f'O resultado da soma de {n1} e {n2} é igual a {n1+n2}')

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='. ')
print(f'Divisão inteira {di} e potência{e}')