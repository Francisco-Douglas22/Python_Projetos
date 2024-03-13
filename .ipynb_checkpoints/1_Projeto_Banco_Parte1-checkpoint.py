# Sistema bancario


menu = '''
MENU DE OPÇÕES
================
[d] Depositar  =
[s] Sacar      =
[e] Extrato    =
[q] Sair       =
================ '''

print(menu)

#Criando as variaveis do Sistema
saldo = 0               #Saldo em Conta
limite = 0              #Limite da Conta
extrato = ""            #Extrato bancario
numero_saque = 0        #Numero do Saque
LIMITE_SAQUE = 3        #Limite diario de saque

#Criando o Loop
while True:

    ver_menu = input("Deseja ver novamente o Menu: [S/N]: ").upper()
    if ver_menu == "S":
        print(menu)

    opcao = input('Digite sua opção: ')

    if opcao == 'd':
        valor = float(input('Informe o valor do Deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print('Operação invalida: Informe um Valor maior que Zero')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Operação Falhou! Saldo insuficiente')
        elif excedeu_limite:
            print('Operação Falhou! O Valor do saque excedeu o limite')
        elif excedeu_saques:
            print('Operação Falhou! Numero maximo de saques excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}'
            numero_saque += 1

        else:
            print('Operação Falhou! O Valor informado e invalido')

    elif opcao == 'e':
        print(f'\n{"="*20} EXTRATO {"="*20}')
        print('Não foram realizados movimentacoes. ' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')

    elif opcao == 'q':
        print('Encerrando Operação Bancaria')
        break

    else:
        print('Operação Invalida, por favor seleciona novamente a opção')





