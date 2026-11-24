print('\t Verificando se você tem "Silva" no seu nome\n')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem "Silva"? {'silva' in nome.lower()}')