def criar_carro(*,modelo, ano,placa,marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

#Formula inválida
#criar_carro('Palio',1999,'ABC-1999',marca='Fiat',motor='1.0', combustivel='Gasolina')

#Formula  válida
criar_carro(modelo='Palio',ano=1999,placa='ABC-1999',marca='Fiat',motor='1.0', combustivel='Gasolina')