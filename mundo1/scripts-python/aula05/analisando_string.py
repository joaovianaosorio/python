frase = 'Curso em Vídeo Python'
print(frase.count('o')) # Conta quantos 'o' tem na frase
print(frase.count('o', 0, 13)) # Conta quantos 'o' tem na frase do caractere de índice 0 até o 13
print(frase.upper().count('O')) # Coloca a frase em maiúsculo e conta quantos 'o' tem na frase
print(frase)
print(frase.find('Python')) # Encontra onde a palavra 'Python' começa
print(frase.find('Android')) # Vai retornar -1 pois não tem a palavra 'Android' no objeto frase
print(frase.find('curso')) # Vai retornar -1 pois 'Curso' começa com C maiúsculo na string
print(frase.lower().find('curso')) # Mudou tudo para minúsculo e vai retornar onde começa a palavra 'curso'
print('Curso' in frase)