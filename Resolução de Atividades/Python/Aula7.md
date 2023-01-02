# Revisão:
## Main:
~~~py
from funcions import *

listaDePedidos = list()
dicionarioDePedidos = dict()

print("Bem vindo ao sistema da lanchote")

while True:

    escolha = int(input("Selecione uma das alternativas a seguir:\n"
                    "1 - Criar pedido\n"
                    "2 - Ver todos os pedidos\n"
                    "3 - Pagamento\n"
                    "0 - Sair\n"))

    match escolha:
        case 1:
            nome = input("qual o seu nome: ")

            listaDePedidos = criacaoDePedido()

            dicionarioDePedidos[nome] = listaDePedidos

        case 2:
            verpedidos(dicionarioDePedidos)

        case 3:

            for i in dicionarioDePedidos:
                print(f"{i} : {dicionarioDePedidos[i]}")

            nome = input("Qual o nome do cliente que está pagando: ")

            pagamento(nome, dicionarioDePedidos)
            del dicionarioDePedidos[nome]

        case 0:
            break
~~~

## Funcions:

~~~py
def criacaoDePedido():
    listaPedido = list()
    listaPedido.clear()
    while True:
        escolha = int(input("Qual o seu pedido seguindo as escolhas a seguir:\n"
                            "1 - Pizza\n"
                            "2 - Lanche\n"
                            "3 - Salgadinho\n"))

        match escolha:
            case 1:
                listaPedido.append("Pizza")

            case 2:
                listaPedido.append("Lanche")

            case 3:
                listaPedido.append("Salgadinho")

        if input("Quer continuar? sim ou não: ").lower() != "sim":
            break

    return listaPedido.copy()


def verpedidos(dicionario):
    for i in dicionario:
        print(f"{i} : {dicionario[i]}")


def pagamento(nome, dicionario):
    pizza = 0
    lanche = 0
    salgadinhos = 0

    for i in dicionario[nome]:
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

        troco = dinheiro - valorTotal

        print(f"Seu troco é de: R${troco},", end=" ")

    print("obrigado e volte sempre")
~~~

https://github.com/GetulioLT/Atividades---l-gica/blob/main/Guias/Python.md
## Menu:
https://github.com/GetulioLT/Atividades---l-gica