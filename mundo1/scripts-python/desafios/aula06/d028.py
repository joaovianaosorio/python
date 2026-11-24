from random import randint
from time import sleep
n_correto = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
n = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3) # Faz o computador esperar
if n == n_correto:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {n_correto} e não no {n}!')