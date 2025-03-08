from constantes import ENTRADA_INVALIDA, CLIENTE_EXISTENTE, AGENCIA, MENU_OPERACOES, OPERACAO_NAO_EXISTENTE, CLIENTE_NAO_EXISTENTE
from operacoes import sacar, depositar, visualizar_extrato
from entidades import PessoaFisica, ContaCorrente

clientes = []
contas = []

def obter_input(mensagem, validar=None):
    while True:
        valor = input(mensagem).strip()
        if (validar and validar(valor)) or validar == None:
            return valor
        
def validar_cpf(cpf):
    cliente_existente = [cliente for cliente in clientes if cliente.cpf == cpf]
    if not cliente_existente:    
        if cpf.isdigit() and len(cpf) == 11:
            return True
        else:
            print(ENTRADA_INVALIDA)
    else:
        print(CLIENTE_EXISTENTE)

def validar_estado(sigla):
    if len(sigla) == 2 and sigla.isalpha():
        return True
    else:
        print(ENTRADA_INVALIDA)

def filtrar_cliente(cpf):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_nova_conta(cliente):
    nova_conta = ContaCorrente(numero=len(contas), cliente=cliente)
    cliente.adicionar_conta(nova_conta)
    contas.append(nova_conta)
    print("\nConta criada com sucesso!\n")

def cadastrar_novo_cliente():
    print("\nPreencha o formulário para cadastro:\n")

    dados = {
        "CPF": obter_input("CPF (Somente números): ", validar_cpf),
        "Nome": obter_input("Nome completo: "),
        "Data de nascimento": obter_input("Data de nascimento (DD/MM/AAAA): "),
        "Logradouro": obter_input("Logradouro: "),
        "Número": obter_input("Número da casa: "),
        "Bairro": obter_input("Bairro: "),
        "Cidade": obter_input("Cidade: "),
        "Estado": obter_input("Sigla do estado (ex: RJ): ", validar_estado)
    }

    cliente = PessoaFisica(dados["CPF"], dados["Nome"],  dados["Data de nascimento"], f"{dados['Logradouro']}, {dados['Número']} - {dados['Bairro']} - {dados['Cidade']}/{dados['Estado']}")
    clientes.append(cliente)
    criar_nova_conta(cliente)

    print("\nCadastro realizado com sucesso!\n")

def acessar_conta():
    cpf = None
  
    while True:
        cpf = input("\nDigite seu CPF (somente números): ")
        cliente = filtrar_cliente(cpf)
        if not cliente:
            print(CLIENTE_NAO_EXISTENTE)
        else:
            break
    
    while True:
        
        opcao = int(input(MENU_OPERACOES))

        if opcao == 1:
            depositar(cliente)

        elif opcao == 2:
            sacar(cliente=cliente)

        elif opcao == 3:
            visualizar_extrato(cliente)
        
        elif opcao == 4:
            criar_nova_conta(cpf)
        
        elif opcao == 0:
            break
        
        else:
            print(OPERACAO_NAO_EXISTENTE)