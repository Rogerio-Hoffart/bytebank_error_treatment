from pprint import pprint
from exceptions import SaldoInsuficienteError

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0

        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo agencia deve ser um inteiro', value)
        if value <= 0:
            raise ValueError('O atributo agencia deve ser maior que zero')
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo numero deve ser um inteiro')
        if value <= 0:
            raise ValueError('O atributo numero deve ser maior que zero')
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo saldo deve ser um número inteiro')
        if value < 0:
            raise ValueError('O atributo saldo não pode ser negativo')
        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError('O valor a ser transferido não pode ser menor que zero(0)', valor)
        self.sacar(valor)
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError('O valor a ser sacado não pode ser menor que zero(0)', valor)
        if (self.saldo < valor):
            raise SaldoInsuficienteError('', saldo=self.saldo, valor=valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

def main():
    import sys

    contas = []
    while(True):
        try:
            nome = input('Nome do Cliente: \n')
            agencia = input('Numero da agencia: \n')
            breakpoint()
            numero = input('Numero da conta corrente: \n')

            cliente = Cliente(nome, None, None)
            conta_corrente = (cliente, agencia, numero)
            contas.append = conta_corrente
        except KeyboardInterrupt:
            print(f'\n\n {len(contas)} conta(s) criada(s)')
            sys.exit()



conta_corrente1 = ContaCorrente(None, 400, 1234567)
conta_corrente2 = ContaCorrente(None, 401, 1234568)

conta_corrente1.transferir(100, conta_corrente2)
print('Conta Corrente1 Saldo: ', conta_corrente1.saldo)
print('Conta Corrente2 Saldo: ', conta_corrente2.saldo)

cliente = Cliente('Jose', '123.456.789-00', 'pintor')

pprint(cliente.__dict__, width=40)
