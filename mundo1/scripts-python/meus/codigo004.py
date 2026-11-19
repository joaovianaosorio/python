print('Joanes'.istitle())              # True  (primeira maiúscula, resto minúscula)
print('João Vitor'.istitle())          # True  (todas as palavras começam com maiúscula)
print('Python Para Iniciantes'.istitle()) # True

print('joanes'.istitle())              # False (tudo minúsculo)
print('JOANES'.istitle())              # False (tudo maiúsculo)
print('João vitor'.istitle())          # False ('vitor' começa com minúscula)
print('João VITOR'.istitle())          # False ('VITOR' tem maiúsculas no meio/fim)