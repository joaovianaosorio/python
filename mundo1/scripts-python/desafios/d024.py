print('\tValidando se você nasceu em uma cidade que começa com a palavra "Santo"\n')
cidade = str(input('Em qual cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')