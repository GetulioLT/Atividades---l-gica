def criacaoDePedido():
    lista Pedido = list()
    listaPedido.clear()
    while True:
        escolha = int(input("Qual o seu pedido seguindo as escolhas a seguir:\n"
                            "1 - Pizza\n"
                            "2 - Lanche\n"
                            "3 - Salgadinho\n"))

        match escolha:
            case 1:
                lista Pedido.append("Pizza")

            case 2:
                lista Pedido.append("Lanche")

            case 3:
                lista Pedido =("Salgadinho")

        if input("Quer continuar? sim ou não: ").lower() != "sim":
            break

    return listaPedido.copy()


def verpedidos(dicionario)
    for i in dicionario:
        print(f"{i} : {dicionario[i]}")


def pagamento(nome, dicionario):
    pizza = 0
    lanche = 0
    salgadinhos = 0

    for i in dicionario[]:
        match i:
            case "Pizza":
                pizza += 1

            case "Lanche":
                lanche += 1

            case "Salgadinho":
                salgadinhos += 1

    valorTotal = (pizza * 25) + (lanche * 10) + (salgadinhos * 5) + 10

    escolha = int(input(f"Valor total é R${valorTotal}\n"
                        "Qual será a forma de pagamento?\n"
                        "1 - Debito\n"
                        "2 - Credito\n"
                        "3 - Dinheiro\n"))

    if escolha == 3:
        dinheiro = int(input("Quanto será o valor entregue? "))

        troco = dinheiro

        print(f"Seu troco é de: R${troco},", end=" ")

    print("obrigado e volte sempre")