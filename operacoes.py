from contantes import VALOR_INVALIDO, LIMITE, LIMITES_SAQUES, SEM_MOVIMENTACAO, LIMITE_SAQUE_EXCEDIDO, LIMITE_VALOR_SAQUE_EXCEDIDO, SALDO_INSUFICIENTE

def depositar(conta, saldo, /):
  novo_saldo = saldo

  valor = float(input("\nValor a ser depositado: R$ "))

  if valor > 0:
    novo_saldo += valor
    conta["operacoes"].append({"deposito": valor})
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return novo_saldo
    
  else:
    print(VALOR_INVALIDO)


def sacar(*, conta, saldo, numero_saques):
  novo_saldo = saldo
  total_saques = numero_saques

  valor = float(input("\nValor a ser sacado: R$ "))

  if valor > 0:
      if valor > LIMITE:
        print(LIMITE_VALOR_SAQUE_EXCEDIDO)

      elif total_saques >= LIMITES_SAQUES:
        print(LIMITE_SAQUE_EXCEDIDO)

      elif valor > novo_saldo:
        print(SALDO_INSUFICIENTE)

      else:
        novo_saldo -= valor
        total_saques += 1
        conta["operacoes"].append({"saque": valor})
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        
      return novo_saldo, total_saques

  else:
      print(VALOR_INVALIDO)

def visualizar_extrato(conta, /, *, saldo):
  print()
  print("EXTRATO".center(36, '='))
    
  if not conta["operacoes"]:
      print(SEM_MOVIMENTACAO)
  else:
      extrato = "\n".join(
          [f"\n{list(op.keys())[0].title()}: R$ {list(op.values())[0]:.2f}" for op in conta["operacoes"]]
      )
      print(extrato)
    
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=".center(36, '='))