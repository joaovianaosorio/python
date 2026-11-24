v = int(input('Qual a velocidade atual do carro? '))
if v > 80:
    valor = (v - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h!')
    print(f'Você deve pagar uma multa de R${valor},00!')
print('Tenha um bom dia! Dirija com segurança')