from contantes import OPERACAO_NAO_EXISTENTE, MENU_PRINCIPAL
from clientes import cadastrar_novo_cliente, acessar_conta

def iniciar_sistema():
  while True:
    opcao = int(input(MENU_PRINCIPAL))

    if opcao == 1:
      acessar_conta()

    elif opcao == 2:
      cadastrar_novo_cliente()
    
    elif opcao == 0:
      break
    
    else:
      print(OPERACAO_NAO_EXISTENTE)

iniciar_sistema()