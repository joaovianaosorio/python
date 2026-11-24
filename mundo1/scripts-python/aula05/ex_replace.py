frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))
print(frase)
# O replace muda uma palavra pela outra
# Porém, o replace só funciona na instância dele, como na linha 8 que está o print()
# O replace não muda de verdade a string

# A não ser que façamos o seguinte:
frase = frase.replace('Python', 'Android')
print(frase)

# Porém, uma string nos seus micro-elementos é imutável
# Se eu colocar frase[0] = 'J', o programa dará erro