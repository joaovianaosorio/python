from math import sqrt

# Se você importa, mas não usa, o PyCharm te dá um aviso
# Normalmente, a linha onde você faz a importação fica com as letras de cor cinza

n = 81

# Quando nós já importamos a função direto, não precisamos colocar o nome da biblioteca antes
# Exemplo: não será mais necessário o "math.sqrt", somente o "sqrt"
raiz = sqrt(n)
print(f'A raíz quadrada de 81 é {raiz:.0f}')