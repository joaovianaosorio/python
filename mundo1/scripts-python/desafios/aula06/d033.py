p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
if p > s and p > t:
    maior = p
elif s > p and s > t:
    maior = s
else:
    maior = t
if p < s and p < t:
    menor = p
elif s < p and s < t:
    menor = s
else:
    menor = t
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')