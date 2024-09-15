#Estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

# IF -> estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if.
#O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas

saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Realizando saque!')

if saldo < saque:
    print('Saldo insuficiente!')

#IF / ELSE -> Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else.
#Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado

saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Realizando saque!')
else:
    print("Saldo insuficiente!")

#IF / ELIF / ELSE -> O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código
# do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais,
#pois elas aumentam a complexidade do código.

opcao = int(input('Informe uma opção: [1] Sacar \n [2] Extrato: '))

if opcao == 1:
    valor = float(input('Informe a quantia para o saque: '))
elif opcao ==2:
    print(input('Exibir o extrato...'))
else:
    print('opção invalida')