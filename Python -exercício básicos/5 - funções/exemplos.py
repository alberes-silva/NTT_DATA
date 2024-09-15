
#Sem argumento
def exibir_mensagem():
    print('Olá mundo"')

#com argumento
def exbir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}')

#Com argumento atribuido diretamente
def exibir_mensagem_3(nome='Anômino'):
    print(f'Seja bem vindo {nome}')

#Chamando as funções
# exibir_mensagem()
# exbir_mensagem_2(nome='Guilherme')
#exibir_mensagem_3() #Se não apresentar o argumento dá erro.
exibir_mensagem_3(nome='Chapie')