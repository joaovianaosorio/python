nome = (input('Digite seu nome: '))
print(f'Olá {nome:20}!')
print(f'Olá {nome:>20}!')   # Deixa texto alinhado a direita
print(f'Olá {nome:<20}!')   # Deixa texto alinhado a esquerda
print(f'Olá {nome:^20}!')   # Deixa texto centralizado
print(f'Olá {nome:=^20}!')  # Deixa texto centralizado no meio dos sinais de igual

# Como o "input" já recebe strings por padrão, não precisamos colocar, nesse caso "str(input())"