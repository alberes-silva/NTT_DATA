#Args vem como tupla, também representado por *
#Kwargs vem como dicionário, também representado por **

def exibir_poema(data_exterso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem= (f'{data_exterso}\n\n{texto}\n\n{meta_dados}')
    print(mensagem)

exibir_poema('Sexta,26 de agosto de 2022',"Zen of Python", "Becautiful is better than ugly.",autor='Tim Peters',ano=1999)