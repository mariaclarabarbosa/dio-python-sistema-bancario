from constantes import AGENCIA, LIMITE, LIMITES_SAQUES, VALOR_INVALIDO, SALDO_INSUFICIENTE, LIMITE_VALOR_SAQUE_EXCEDIDO, LIMITE_SAQUE_EXCEDIDO
from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        status_sucesso = conta.depositar(self._valor)
        if status_sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        status_sucesso = conta.sacar(self._valor)
        if status_sucesso:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = AGENCIA
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        if valor > self._saldo:
            print(SALDO_INSUFICIENTE)
            return False
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):
        if valor < 0:
            print(VALOR_INVALIDO)
            return False
        else:
            self._saldo += valor
            return True
    
class ContaCorrente(Conta):
    def __init__(self, limite = LIMITE, limite_saque = LIMITES_SAQUES, **kwards):
        super().__init__(**kwards)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])

        if valor < 0:
            print(VALOR_INVALIDO)
            return False
        elif valor > self._limite:
            print(LIMITE_VALOR_SAQUE_EXCEDIDO)
            return False
        elif numero_saques >= self._limite_saque:
            print(LIMITE_SAQUE_EXCEDIDO)
            return False
        else:
            return super().sacar(valor)


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    @property
    def contas(self):
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf