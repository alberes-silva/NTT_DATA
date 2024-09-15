#Estruturas FOR e WHILE
#For é utilizado quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando
#queremos percorrer um objeto iterável

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'
contador = 0

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
        contador +=1
        
else:
    print()
    print(contador)