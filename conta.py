

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Conta criada.{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print ('O titular {} possui um saldo de: R${} e um limite de R${}'.format(self.__titular,self.__saldo,self.__limite))

    def deposita(self, valor):
         self.__saldo += valor

    def saca (self, valor):
         self.__saldo -= valor

    def transfere (self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def print_saldo(self):
       return self.__saldo

    def print_titular(self):
        return self.__titular

    def print_limite(self):
     return self.__limite

    def modifica_limite(self,limite):
         self.__limite = limite




