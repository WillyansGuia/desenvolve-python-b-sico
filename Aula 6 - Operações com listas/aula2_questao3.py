#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:

#Ambas as listas

#A lista intersecção ordenada

#A quantidade de vezes que cada elemento aparece em cada lista

#Atenção, a lista de intersecções não pode ter duplicatas.

#lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]

#lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]

#Interseccao - [10, 11, 20]

#Contagem

#10: (lista1=4, lista2=1)

#11: (lista1=1, lista2=2)

#20: (lista1=1, lista2=1)

import random

# Criando as duas listas com 20 valores aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criando a lista de interseção sem duplicatas usando set
interseccao = sorted(list(set(lista1) & set(lista2)))

# Imprimindo as listas
print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")
print(f"\nInterseccao - {interseccao}")

# Contagem e impressão das ocorrências
print("\nContagem:")
for elemento in interseccao:
    count1 = lista1.count(elemento)
    count2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={count1}, lista2={count2})")
    