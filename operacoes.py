from constantes import VALOR_INVALIDO, LIMITE, LIMITES_SAQUES, SEM_MOVIMENTACAO, LIMITE_SAQUE_EXCEDIDO, LIMITE_VALOR_SAQUE_EXCEDIDO, SALDO_INSUFICIENTE
from entidades import Deposito, Saque

def recuperar_conta_cliente(cliente):
    return cliente.contas[0]

def depositar(cliente, /):
  valor = float(input("\nValor a ser depositado: R$ "))
  transacao = Deposito(valor)
  conta = recuperar_conta_cliente(cliente)
  cliente.realizar_transacao(conta, transacao)
  


def sacar(*, cliente):
  valor = float(input("\nValor a ser sacado: R$ "))
  transacao = Saque(valor)
  conta = recuperar_conta_cliente(cliente)
  cliente.realizar_transacao(conta, transacao)


def visualizar_extrato(cliente):
  conta = recuperar_conta_cliente(cliente)
  transacoes = conta.historico.transacoes
  extrato = ""

  print()
  print("EXTRATO".center(36, '='))
    
  if not transacoes:
      extrato = SEM_MOVIMENTACAO
  else:
      for transacao in transacoes:
        extrato += f"\n{transacao['tipo']}:\tR${transacao['valor']:.2f}"
  
  print(extrato)  
  print(f"\nSaldo: R$ {conta.saldo:.2f}")
  print("=".center(36, '='))