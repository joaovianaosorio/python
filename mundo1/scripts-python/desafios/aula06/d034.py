s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250.00:
    sn = s * 0.15 + s
else:
    sn = s * 0.1 + s
print(f'Quem gan9hava R${s} passa a ganhar R${sn} agora.')