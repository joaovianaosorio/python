nome = str(input('Digite seu nome: '))
print('Olá {:20}!'.format(nome))
print('Olá {:>20}!'.format(nome)) # Deixa texto alinhado a esquerda
print('Olá {:<20}!'.format(nome)) # Deixa texto alinhado a direita
print('Olá {:^20}!'.format(nome)) # Deixa texto centralizado
print('Olá {:=^20}!'.format(nome)) # Deixa texto centralizado no meio dos sinais de igual