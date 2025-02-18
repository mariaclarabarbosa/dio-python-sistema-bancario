# Desafio: Sistema Bancário v1  

Este projeto foi desenvolvido como parte de um desafio para implementar um **sistema bancário básico** utilizando a linguagem **Python**. O sistema contém as operações de depósito, saque e extrato, seguindo as regras definidas pelo banco contratante.  

## 📋 Descrição do Desafio  

Fomos contratados por um grande banco para desenvolver o seu novo sistema bancário, com o objetivo de modernizar suas operações. Para a primeira versão do sistema (v1), precisamos implementar três operações principais:  

1. **Depósito**  
2. **Saque**  
3. **Extrato**  

---

## ⚙️ Regras de Implementação  

### Depósito  
- Deve ser possível depositar **apenas valores positivos**.  
- O sistema trabalha com **um único usuário** e não precisa identificar agência ou número da conta bancária.  
- Todos os depósitos realizados devem ser armazenados em uma variável e exibidos no extrato.  

### Saque  
- Limite de **3 saques diários**.  
- Valor máximo de saque por operação: **R$ 500,00**.  
- Caso o usuário não tenha saldo suficiente, o sistema deve exibir uma mensagem indicando a **falta de saldo**.  
- Todos os saques devem ser armazenados em uma variável e exibidos no extrato.  

### Extrato  
- O extrato deve listar todos os **depósitos e saques** realizados.  
- No final da listagem, deve ser exibido o **saldo atual** da conta.  
- Se o extrato estiver vazio (sem movimentações), deve ser exibida a mensagem:  
  - `"Não foram realizadas movimentações."`  
- Os valores exibidos no extrato devem seguir o formato: `R$ xxx.xx`.  
  - Exemplo: `1500.45` será exibido como `R$ 1500.45`.  

---

## 🛠️ Tecnologias Utilizadas  

- **Linguagem**: Python 3
