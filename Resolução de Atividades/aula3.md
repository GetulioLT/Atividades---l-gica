# Entrada e Saída de dados:
## Questão 1:
~~~python
peso = float(input('Digite seu peso: '))
altura = float(input('Digite seu altura: '))

imc = peso / altura ** 2

print(f'seu imc é igual : {imc}')
~~~
## Questão 2:
~~~python
tf = float(input('Digite a temperatura em fahrenheit: '))

tc = (tf - 32) / 1.8

print(f'A temperatura em celcis é igual a: {tc}')
~~~
## Questão 3:
~~~python
largura = float(input('Digite a largura do retangulo: '))
comprimento = float(input('Digite a comprimento do retangulo: '))

retangulo = largura * comprimento

print(f'A area do Retângulo é igua a: {retangulo}')
~~~
## Questão 4:
~~~python
vBrancos = int(input('Digite a quantidade de votos Brancos: '))
vNulos = int(input('Digite a quantidade de votos Nulos: '))
vValidos = int(input('Digite a quantidade de votos Validos: '))

total = vValidos + vNulos + vBrancos

pValidos = vValidos / total * 100
pBrancos = vBrancos / total * 100
pNulos = vNulos / total * 100

print(f'O percente de votos \n' +
f'Votos Validos: {pValidos}' +
f'Votos Brancos: {pBrancos}' +
f'Votos Nulos: {pNulos}')
~~~

# Condicionais:
## Questão 1:
~~~py
