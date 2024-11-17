import json
from datetime import datetime

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {"receitas": [], "despesas": []}

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função para adicionar uma nova receita
def adicionar_receita(dados):
    descricao = input("Descrição da receita: ")
    valor = float(input("Valor da receita: "))
    data = input("Data da receita (YYYY-MM-DD): ")

    receita = {
        "id": len(dados["receitas"]) + 1,
        "descricao": descricao,
        "valor": valor,
        "data": data
    }
    dados["receitas"].append(receita)
    salvar_dados(dados)
    print(f"Receita '{descricao}' de R$ {valor} registrada com sucesso!")

# Função para adicionar uma nova despesa
def adicionar_despesa(dados):
    descricao = input("Descrição da despesa: ")
    valor = float(input("Valor da despesa: "))
    data = input("Data da despesa (YYYY-MM-DD): ")

    despesa = {
        "id": len(dados["despesas"]) + 1,
        "descricao": descricao,
        "valor": valor,
        "data": data
    }
    dados["despesas"].append(despesa)
    salvar_dados(dados)
    print(f"Despesa '{descricao}' de R$ {valor} registrada com sucesso!")

# Função para calcular o saldo atual
def calcular_saldo(dados):
    total_receitas = sum([receita["valor"] for receita in dados["receitas"]])
    total_despesas = sum([despesa["valor"] for despesa in dados["despesas"]])
    saldo = total_receitas - total_despesas
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função principal para exibir o menu e gerenciar o sistema
def menu():
    dados = carregar_dados()
    
    while True:
        print("\n--- Sistema de Controle Financeiro ---")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Verificar Saldo Atual")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_receita(dados)
        elif opcao == '2':
            adicionar_despesa(dados)
        elif opcao == '3':
            calcular_saldo(dados)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
