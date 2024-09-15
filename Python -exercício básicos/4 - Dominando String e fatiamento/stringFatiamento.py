curso = 'pYtHon'

#Deixa todas as letras maisculas
print(curso.upper())

#Deixa todas as letras minusculas
print(curso.lower())

#Deixa em título ou a primeira letra maisculas
print(curso.title())
print(curso.capitalize())

curso2 = ' Python'

#Retirando o espaço em branco nem no ínicio, nem no fim
print(curso2.strip())

#remover espaço da esquerda
print(curso2.lstrip())

#remover espaço da direita
print(curso2.rstrip())

print(curso2.center(10,'#'))

print('.'.join(curso2))