print('********************************************************\n')
print('                    Sistema Bancário\n')
print('********************************************************\n')


menu = '''
Escolha a operação:
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

==> '''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3


while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Digite o valor do deposito R$ '))
        if valor > 0:
            saldo += valor
            print(f'Depósitado realizado com sucesso!\n')
            extrato += (f'Depósito: R${valor}\n')
        else:
            print('Operação falhou! O valor informado é inválido')
    elif opcao == '2':
        valor = float(input('Digite o valor do saque R$ '))
        excede_valor = valor > saldo
        excede_limite = valor > limite
        excede_saques = numero_saque >= limite_saque

        if excede_valor:
            print(f'Operação falhou! Você não tem saldo suficiente. Seu saldo é R${saldo}')
        elif excede_limite:
             print(f'Operação falhou! O valor do saque excede o seu limite. Seu saldo é R${saldo}')
        elif excede_saques:
             print(f'Operação falhou! Você excedeu o numero de 3 saques diários. Quantidade de saques realizado {numero_saque}')    

        elif valor > 0:
            saldo -= valor
            print(f'Saque realizado com sucesso!\n')
            extrato += (f'Saque: R${valor:.2f}\n')
            numero_saque += 1
        else:
            print('Operação falhou! O valor informado é inválido.')
    elif opcao == '3':
        print('********************************************************\n')
        print('                    Extrato Bancário\n')
        print('********************************************************\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}\n')
        print('                    Agradecemos a sua confiança\n')
        print('********************************************************\n')
    elif opcao == '4':
        print('Finalizada a operação')
        break
    else:
        print('Opção inválida, tente novamente')
