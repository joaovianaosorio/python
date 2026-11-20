d = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km foram rodados? '))
valor_d = d * 60
valor_km = km * 0.15
t = valor_d + valor_km
print(f'O total a pagar é de R${t:.2f}')