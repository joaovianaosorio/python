print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p > s and p > t:
    maior = p
    menores = s + t
elif s > p and s > t:
    maior = s
    menores = p + t
else:
    maior = t
    menores = p + s
if menores > maior:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')