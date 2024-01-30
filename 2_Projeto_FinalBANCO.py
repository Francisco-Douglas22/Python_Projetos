# Importa o módulo uuid para gerar identificadores únicos
import uuid
# Importa o módulo datetime para trabalhar com datas
import datetime






# Classe para representar as informações de um usuário
class Usuario:
    # Método de inicialização
    def __init__(self, nome, endereco, cpf, idade):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.idade = idade

    # Método para exibir informações do usuário
    def exibir_informacoes(self):
        print(f"\n===== Informações do Usuário =====")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade} anos")










# Classe base para contas bancárias
class ContaBancaria:
    # Método de inicialização
    def __init__(self, numero_conta, usuario, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = saldo_inicial
        self.limite_diario = 2000.0
        self.limite_saques_diarios = 4
        self.saques_realizados = 0
        self.ultimo_saque_data = None

    # Método para realizar depósito
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    # Método para realizar saque
    def sacar(self, valor):
        # Verifica se atingiu o limite de saques diários
        if self.saques_realizados >= self.limite_saques_diarios:
            print('Limite de saques diários atingido.')
            return

        # Verifica se o valor do saque ultrapassa o limite diário
        if valor > self.limite_diario:
            print(f'Limite de saque diário excedido (limite: R${self.limite_diario}).')
        # Verifica se o saldo é suficiente
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            # Verifica se a data do último saque é diferente da data atual
            hoje = datetime.date.today()
            if self.ultimo_saque_data != hoje:
                self.ultimo_saque_data = hoje
                self.saques_realizados = 0  # Zera o contador de saques diários

            # Realiza o saque e atualiza os contadores
            self.saldo -= valor
            self.saques_realizados += 1
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')

    # Método para consultar o saldo
    def consultar_saldo(self):
        print(f'Saldo da conta {self.numero_conta}: R${self.saldo}')

    # Método para realizar transferência para outra conta
    def transferir(self, destino, valor):
        # Verifica se há saldo suficiente para a transferência
        if valor > self.saldo:
            print('Saldo insuficiente para transferência.')
        else:
            # Realiza a transferência
            self.saldo -= valor
            destino.depositar(valor)
            print(f'Transferência de R${valor} realizada para conta {destino.numero_conta}.')







# Classe derivada para conta corrente que herda de ContaBancaria
class ContaCorrente(ContaBancaria):
    # Método de inicialização da conta corrente
    def __init__(self, numero_conta, usuario, saldo_inicial=0.0, limite=500.0):
        # Chama o método de inicialização da classe base
        super().__init__(numero_conta, usuario, saldo_inicial)
        # Atributo adicional para o limite da conta corrente
        self.limite = limite

    # Sobrescreve o método sacar para considerar o limite da conta corrente
    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')





# Classe para representar o banco, que gerencia as contas
class Banco:
    # Método de inicialização do banco
    def __init__(self):
        # Dicionário para armazenar as contas com seus números como chaves
        self.contas = {}

    # Método para cadastrar uma nova conta no banco
    def cadastrar_conta(self, conta):
        self.contas[conta.numero_conta] = conta

    # Método para buscar uma conta no banco usando o número da conta
    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)






# Função para exibir o menu principal
def exibir_menu():
    print("\n===== Menu =====")
    print("1. Criar Conta")
    print("2. Acessar Conta")
    print("3. Sair")









# Função para criar um usuário com base na entrada do usuário
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    endereco = input("Digite o endereço do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    return Usuario(nome, endereco, cpf, idade)








# Função para criar uma conta com base na escolha do usuário
def criar_conta(banco):
    usuario = criar_usuario()
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    tipo_conta = input("Escolha o tipo de conta (1 - Conta Bancária, 2 - Conta Corrente): ")

    numero_conta = str(uuid.uuid4())

    if tipo_conta == '1':
        conta = ContaBancaria(numero_conta, usuario, saldo_inicial)
    elif tipo_conta == '2':
        limite = float(input("Digite o limite da conta corrente: "))
        conta = ContaCorrente(numero_conta, usuario, saldo_inicial, limite)
    else:
        print("Opção inválida. Conta bancária padrão criada.")
        conta = ContaBancaria(numero_conta, usuario, saldo_inicial)

    banco.cadastrar_conta(conta)
    print(f'\nConta criada com sucesso! Número da conta: {numero_conta}')










# Função para acessar uma conta existente e realizar operações
def acessar_conta(banco):
    numero_conta = input("Digite o número da conta: ")
    conta = banco.buscar_conta(numero_conta)

    if conta:
        while True:
            print("\n===== Menu da Conta =====")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Consultar Saldo")
            print("4. Transferir")
            print("5. Exibir Informações do Usuário")
            print("6. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Digite o valor do depósito: "))
                conta.depositar(valor)
            elif opcao == '2':
                valor = float(input("Digite o valor do saque: "))
                conta.sacar(valor)
            elif opcao == '3':
                conta.consultar_saldo()
            elif opcao == '4':
                dest_conta = input("Digite o número da conta de destino: ")
                dest_conta = banco.buscar_conta(dest_conta)
                if dest_conta:
                    valor = float(input("Digite o valor da transferência: "))
                    conta.transferir(dest_conta, valor)
                else:
                    print("Conta de destino não encontrada.")
            elif opcao == '5':
                conta.usuario.exibir_informacoes()
            elif opcao == '6':
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Conta não encontrada.")












# Função principal que inicia o sistema bancário
def main():
    # Cria uma instância do banco
    banco = Banco()

    # Loop principal do programa
    while True:
        # Exibe o menu principal
        exibir_menu()
        # Solicita ao usuário que escolha uma opção
        escolha = input("Escolha uma opção: ")

        # Executa a operação correspondente à escolha do usuário
        if escolha == '1':
            criar_conta(banco)
        elif escolha == '2':
            acessar_conta(banco)
        elif escolha == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia a execução do programa
if __name__ == "__main__":
    main()
