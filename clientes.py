from contantes import ENTRADA_INVALIDA, CLIENTE_EXISTENTE, AGENCIA, MENU_OPERACOES, OPERACAO_NAO_EXISTENTE, CLIENTE_NAO_EXISTENTE
from operacoes import sacar, depositar, visualizar_extrato

clientes = {}
contas_correntes = []

def obter_input(mensagem, validar=None):
    while True:
        valor = input(mensagem).strip()
        if (validar and validar(valor)) or validar == None:
            return valor
        
def validar_cpf(cpf):
    if not clientes.get(cpf):    
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

def filtrar_conta_corrente(cpf):
    conta_corrente_filtradas = [conta for conta in contas_correntes if conta['usuario']['cpf'] == cpf]
    return conta_corrente_filtradas[0] if conta_corrente_filtradas else None

def criar_nova_conta(cpf):
    usuario = clientes.get(cpf)
    usuario['cpf'] = cpf
    contas_correntes.append({"agencia": AGENCIA, "numero_da_conta": len(contas_correntes) + 1, "usuario": usuario, "operacoes": []})
    print("\nConta corrente criada com sucesso!\n")

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

    clientes.update({dados["CPF"]: { 
        "nome": dados["Nome"], 
        "data_nascimento": dados["Data de nascimento"],
        "endereco": f"{dados['Logradouro']}, {dados['Número']} - {dados['Bairro']} - {dados['Cidade']}/{dados['Estado']}"
    }})
    criar_nova_conta(dados["CPF"])

    print("\nCadastro realizado com sucesso!\n")

def acessar_conta():
    cpf = None
    saldo = 0.0
    numero_saque = 0
    conta_corrente = None
  
    while True:
        cpf = input("\nDigite seu CPF (somente números): ")
        conta_corrente = filtrar_conta_corrente(cpf)
        if cpf not in clientes:
            print(CLIENTE_NAO_EXISTENTE)
        else:
            break
    
    while True:
        
        opcao = int(input(MENU_OPERACOES))

        if opcao == 1:
            saldo = depositar(conta_corrente, saldo)

        elif opcao == 2:
            saldo, numero_saque = sacar(conta=conta_corrente, saldo=saldo, numero_saques=numero_saque)

        elif opcao == 3:
            visualizar_extrato(conta_corrente, saldo=saldo)
        
        elif opcao == 4:
            criar_nova_conta(cpf)
        
        elif opcao == 0:
            break
        
        else:
            print(OPERACAO_NAO_EXISTENTE)