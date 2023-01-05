# Função:
## Questão 1:
~~~py
def tempo(seg):
    horas = seg // 3600
    seg -= horas * 3600

    min = seg // 60
    seg -= min * 60

    return f"O total do tempo é de: {horas}:{min}:{seg}"


segundos = int(input("Digite o tempo total da fabrica em segundos: "))

print(tempo(segundos))
~~~
## Questão 2:
~~~py
def idade(anos, meses, dias):
    total = (anos * 365) + (meses * 30) + dias

    return total

anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
dias = int(input("Digite a quantidade de dias: "))

print(idade(anos, meses, dias))
~~~
## Questão 3:
~~~py
def verificacao(num):
    if num > 0:
        return "Positivo e par" if num % 2 == 0 else "Positivo e impar"
    else:
        return "Negativo"


numero = int(input("Digite um numero inteiro qualquer: "))

print(verificacao(numero))
~~~
## Questão 4:
~~~py
def volume(raio):
    v = (4 / 3) * 3.14 * (raio ** 2)

    return v

raio = float(input("Digite o raio da circuferencia: "))

print(volume(raio))
~~~
## Questão 5:
~~~py
def fatorial(num):
    acumulativo = 1
    for i in range(num, 0, -1):
        acumulativo *= i

    return acumulativo

numero = int(input("Digite o numero para descobrir seu fatorial: "))

print(fatorial(numero))
~~~
## Desafio:
~~~py
def somatorio(n):
    acumulativo = 0
    texto = ""
    for i in range(1, n + 1):
        if i == 1:
            texto += "S = 1"
            acumulativo += 1
        else:
            texto += f" + 1/{i}"
            acumulativo += 1 / i
    else:
        texto += f" = {acumulativo:.2f}"

    return texto

numero = int(input("Digite um numero inteiro e positivo qualquer: "))

print(somatorio(numero))
~~~

https://github.com/GetulioLT/Atividades---l-gica/blob/main/Guias/Python.md
## Menu:
https://github.com/GetulioLT/Atividades---l-gica