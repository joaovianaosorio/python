from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
co_elevado = co ** 2
ca_elevado = ca ** 2
h = co_elevado + ca_elevado
h_real = sqrt(h)
print(f'A hipotenusa vai medir aproximadamente {h_real:.2f}')