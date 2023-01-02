lista de pedidos = list()
dicionario de pedidos = dict()

print("Bem vindo ao sistema da lanchote")

while True:

    escolha = input("Selecione uma das alternativas a seguir:\n"
                    "1 - Criar pedido\n"
                    "2 - Ver todos os pedidos\n"
                    "3 - Pagamento\n"
                    "0 - Sair")

    match escolha:
        case 1:
            nome = input("qual o seu nome: ")

            lista de pedidos = criaçao de pedido(nome)


        case 2:
            ver pedidos(dicionario de pedidos)

        case 3:
            nome = input("Qual o nome do cliente que está pagando: ")

            pagamento(nome, dicionario de pedidos)

        case 0:
            break