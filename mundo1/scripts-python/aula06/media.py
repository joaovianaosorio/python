n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print(f'Sua média foi {m:.2f}')
if m>7:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')