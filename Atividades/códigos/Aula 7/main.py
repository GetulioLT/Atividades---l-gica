lista De Pedidos = list()
dicionario De Pedidos = dict()

print("Bem vindo ao sistema da lanchote")

while True:

    escolha = input("Selecione uma das alternativas a seguir:\n"
                    "1 - Criar pedido\n"
                    "2 - Ver todos os pedidos\n"
                    "3 - Pagamento\n"
                    "0 - Sair\n")

    match escolha:
        case 1:
            nome = input("qual o seu nome: ")

            lista De Pedidos = criacaoDePedido()

            dicionario DePedidos[nome] = listaDePedidos

        case 2:
            verpedidos()

        case 3:

            for i in dicionarioDePedidos:
                print(f"{i} : {dicionarioDePedidos[i]}")

            nome = input("Qual o nome do cliente que está pagando: ")

            pagamento(nome, dicionarioDePedidos)

        case 0:
            break