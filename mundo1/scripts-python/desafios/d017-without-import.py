co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adajacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))