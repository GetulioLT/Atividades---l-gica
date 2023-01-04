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

https://github.com/GetulioLT/Atividades---l-gica/blob/main/Guias/Python.md
## Menu:
https://github.com/GetulioLT/Atividades---l-gica