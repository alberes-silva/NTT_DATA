#Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe.
#Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados
#(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (clousures).


def somar(a,b):
    return a + b

def subtrair(a,b):
    return a-b

def test(a,b):
    return a * 2 + b * 3

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação é = {resultado}')

exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)
# exibir_resultado(10,10,test)

op = somar
print(op(1,23))