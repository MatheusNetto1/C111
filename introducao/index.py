#  -------------------------------- Comando print
print('hello world')
print(7+7)
print('O resultado de 7 + 7 é: ', 7+7) # para imprimir mais de uma coisa,  usamos vírgula

#  -------------------------------- Variáveis

nome = 'Matheus Netto'
idade = 24
peso = 85.1

print(f'Seu nome é: {nome}, você tem {idade} anos, e pesa {peso:.2f}kg.')

#  -------------------------------- Leitura

nome = input('Digite seu nome: ')
idade = int(input('Qual a sua idade? '))
peso = float(input('Peso: '))

print(f'Seu nome é: {nome}, você tem {idade} anos, e pesa {peso:.2f} kg.')

print(type(nome))
print(type(idade))
print(type(peso))

#  -------------------------------- Operadores

x = int(input('Digite x: '))
y = int(input('Digite y: '))

soma = x+y;
subtracao = x-y
multiplicacao = x*y
divisao = x/y

divisao_inteira = x//y
potencia = x**y
resto = x%y

print(f'soma é: {soma}')
print(f'subtração é: {subtracao}')
print(f'multiplicação é: {multiplicacao}')
print(f'divisão é: {divisao}')

print(f'divisão inteira é: {divisao_inteira}')
print(f'potência é: {potencia}')
print(f'resto é: {resto}')

#  -------------------------------- Bibliotecas

import math as m

x = float(input('Digite x: '))

print(m.trunc(x))

print(m.trunc(x), m.ceil(x), m.floor(x), round(x, 2))

#  -------------------------------- Cadeias de caracteres

var = 'Hello world'
print(var[6]) # mostra a letra 'w'
print(var[6:11]) # mostra da posição 6 até a posição 10
print(var[6:]) # mostra da posição 6 até o final
print(var[0:11:2]) # mostra da posição 0 até a posição 10 pulando de 2 em 2

#  -------------------------------- Funções úteis

var = 'Hello world'
print(len(var)) # comprimento de var
print(var.count('o')) # conta quantos 'o'
print(var.count('l', 0, 5)) # conta quantos 'l' no intervalo [0, 4]
print(var.find('lo')) # posição onde está 'lo'
print('world' in var) # True se 'world' estiver em var
var1 = var.replace('world', 'Python') # troca 'world' por 'Python'
print(var1)
print(var.upper()) # maiúsculas
print(var.lower()) # minúsculas