menu = """
Selecione a opção que gostaria de realizar:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Operação: """

LIMITE = 500
LIMITES_SAQUES = 3

saldo = 0
numero_saques = 0
operacoes_realizadas = []


while True:
  opcao = int(input(menu))

  if opcao == 1:
    valor = float(input("\nValor a ser depositado: R$ "))
    
    if valor > 0:
      saldo += valor
      operacoes_realizadas.append({"deposito": valor})
      print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    
    else:
      print("Falha na operação! O valor informado é inválido.")

  elif opcao == 2:
    valor = float(input("\nValor a ser sacado: R$ "))

    if valor > 0:

      if valor > LIMITE:
        print("Falha na operação! O valor do saque excede o limite.")

      elif numero_saques >= LIMITES_SAQUES:
        print("Falha na operação! Número máximo de saques excedidos.")

      elif valor > saldo:
        print("Falha na operação! Saldo insuficiente.")

      else:
        saldo -= valor
        numero_saques += 1
        operacoes_realizadas.append({"saque": valor})
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    else:
      print("Falha na operação! O valor informado é inválido.")

  elif opcao == 3:
    print()
    print("EXTRATO".center(36, '='))
    
    if not operacoes_realizadas:
        print("\nNão foram realizadas movimentações.")
    else:
        extrato = "\n".join(
            [f"\n{list(op.keys())[0].title()}: R$ {list(op.values())[0]:.2f}" for op in operacoes_realizadas]
        )
        print(extrato)
    
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=".center(36, '='))
  
  elif opcao == 0:
    break
  
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")