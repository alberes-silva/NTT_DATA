#Função range -> É uma função Built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio(inclusive)
#para um fim(exclusivo). Se usarmos range(i,j) será produzido:
#i,i+1,i+2,i+3...,j-1.
#Ela recebe 3 argumentos : stop(obrigatório), start (opcional) e step (opcional)


# print(list(range(4)))

# for numero in range (0,11):
#     print(numero, end=' ')


# for numero in range (0,51,5):
#     print(numero, end=' ')

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=' ')
    
