# Dicionario:
## Questão 1:
~~~py
alunos = dict()

for i in range(5):
    nome = input("Digite o seu nome: ")

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3

    alunos[nome] = float(f"{media:.2f}")
    
print(alunos)

print("===============================================")

alunos = dict()

for i in range(5):
    nome = input("Digite o seu nome: ")

    acumulador = 0

    for j in range(3):
        nota = float(input(f"Digite a {j + 1}° nota: "))

        acumulador += nota 

    media = acumulador / 3

    alunos[nome] = float(f"{media:.2f}")
    
print(alunos)
~~~

## Questão 2:
~~~py
agenda = dict()

print("Bem vindo a agenda telefonica.")

while True:
    nome = input("Digite o nome da pessoa: ")

    numero = int(input("Digite agora o numero da pessoa: "))

    agenda[nome] = numero

    escolha = input("Digite s para adicionar uma nova pessoa e n para finalizar a agenda: ")

    if escolha.lower() == "n":
        break


for i in agenda:
    print(f"{i} : {agenda[i]}")
~~~

## Questão 3:
~~~py
num_paciente = 1
pacientes = dict()
info = list()

print("Bem vindo ao sistem médico.")

while True:
    escolha = int(input("Digite uma das opções abaixo:\n"
                        "1 - Cadastrar novo paciente;\n"
                        "2 - Ver todos os pacientes;\n"
                        "3 - Apagar um paciente;\n"
                        "0 - Sair do sistema.\n"))

    match escolha:
        case 1:
            nome = input("Digite o nome do paciente: ")
            idade = int(input("Digite a idade do paciente: "))
            peso = float(input("Digite o peso do paciente: "))
            altura = float(input("Digite a altura do paciente: "))

            info= [f"nome = {nome}", f"idade = {idade}", f"peso = {peso}", f"altura = {altura}"]

            pacientes[num_paciente] = info

            num_paciente += 1

            input("Cadastro feito com sucesso. Aperte enter para continuar...")

        case 2:
            for i in pacientes:
                print(f"id: {i} - informações: {pacientes[i]}")

            input("Aperte enter para continuar...")

        case 3:
            for i in pacientes:
                print(f"id: {i} - informações: {pacientes[i][0]}")

            id = int(input("Digite qual id quer apagar: "))

            pacientes.pop(id)

            input("Paciente apagado com sucesso. Aperte enter para continuar...")

        case 0:
            break

    print("\n"* 20)
~~~

https://github.com/GetulioLT/Atividades---l-gica/blob/main/Guias/Python.md
## Menu:
https://github.com/GetulioLT/Atividades---l-gica