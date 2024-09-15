# def sacar(self, valor: float) -> None:
#     if self.saldo >= valor:
#         self.saldo -= valor


def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print('Valor sacado!')
        print("Retire o seu dinheiro na boca do caixa")

    print('Obrigado por ser nosso cliente, tenha um bom dia!')

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Seu novo saldo é {saldo}')


sacar(100)
depositar(1000)