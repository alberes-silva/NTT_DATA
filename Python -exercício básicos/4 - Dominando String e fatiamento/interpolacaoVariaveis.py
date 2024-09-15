#Exsite 3 formas de interpolação, %, format e f strings

#% menos usada
nome = 'Guilherme'
idade = 28
profissao = 'Programador'
linguagem = 'Python'

#%
print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho  com %s e estou matriculado no curso de %s.' %(nome, idade, profissao, linguagem))

#.format
print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho  com {} e estou matriculado no curso de {}.' .format(nome, idade, profissao, linguagem))

#f strings
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho  com {profissao} e estou matriculado no curso de {linguagem}.')

PI = 3.14159

print(f'Valor de PI: {PI:.2f}')

print(f'Valor de PI: {PI:10.2f}')

