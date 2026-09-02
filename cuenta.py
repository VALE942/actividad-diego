class cuenta:
    def __init__(self, saldo, numero):#constructor
        self.__saldo = saldo
        self.numero = numero

    def depositar(self, cantidad):#metodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("cantidad invalida")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("fondos insuficientes")

    #agregar metodo para imprimir el saldo

    def imprimirsaldo(self):
        print(f"el saldo de la cuenta {self.numero} es: {self.__saldo}")


#creacion de cuienta
cuenta1 = cuenta(1000, 12345)
print(cuenta1.numero)
cuenta1.depositar(2000)
print(cuenta1.numero)
cuenta1.retirar(6000)
print (cuenta1.imprimirsaldo())

