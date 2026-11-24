# Expressão condicional ou operador ternário
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print(f'Sua média foi {m:.2f}')
print('Parabéns' if m>7 else 'Estude mais')