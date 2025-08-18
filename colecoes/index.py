#  -------------------------------- Tuplas

nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan') # declara a tupla

print(nomes) # printa a lista
print(nomes[1]) # printa o Vegeta
print(nomes[:2]) # printa os dois primeiros
print(len(nomes)) # printa a quantidade de nomes na lista

print(sorted(nomes)) # printa em ordem alfabética

#  -------------------------------- Listas

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan'] # declara a lista

nomes.append('Bulma') # adiciona Bulma no final da lista
# nomes[1] = 'Kiririn' # substitui Vegeta por Kiririn
nomes.insert(1, 'Kiririn') # adiciona Kiririn na posição 1 sem substituir ninguém
nomes.remove('Goku') # remove Goku

print(sorted(nomes)) # printa en ordem alfabética mas não ordena a lista

nomes.sort() # ordena a lista
print(nomes)

#  -------------------------------- Conjuntos

nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Trunks', 'Goku'} # declara o conjunto
nomes.add('Kiririn') # adiciona Kiririn
nomes.remove('Goku') # remove Goku

print(nomes)

#  -------------------------------- Conjuntos 2

A = {1, 2, 4}
B = {3, 4, 6}

Uniao = A | B
Interseccao = A & B
Diferenca = A - B

print(Uniao)
print(Interseccao)
print(Diferenca)

#  -------------------------------- Dicionário

dados = {'nome': 'Goku', 'idade': 43}
dados['sexo'] = 'M'

print(dados['nome'])
print(dados['sexo'])
print(dados.keys())

#  -------------------------------- Exercício 1

dados1 = {'nome': 'Goku', 'idade': 43, 'sexo': 'M'}
dados2 = {'nome': 'Vegeta', 'idade': 23, 'sexo': 'M'}
dados3 = {'nome': 'Bulma', 'idade': 50, 'sexo': 'F'}

dbz = [dados1, dados2, dados3]

print(dbz[0]['nome'])
print(dbz[1]['idade'])
print(dbz[2]['sexo'])