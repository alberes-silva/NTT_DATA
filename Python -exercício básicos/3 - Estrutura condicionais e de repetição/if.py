maior_idade = 18

idade = int(input("Informe a sua idade: "))

if idade >= 18:
    print('Maior de idade, pode tirar a CNH')


if idade < maior_idade:
    print("Ainda não pode tirar a CNH")