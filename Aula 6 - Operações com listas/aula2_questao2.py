#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:

#A lista elementos

#A soma dos valores da lista

#A média dos valores da lista

import random

# Gera um valor aleatório entre 5 e 20 para num_elementos
num_elementos = random.randint(5, 20)

# Gera valores aleatórios entre 1 e 10 e armazena na lista elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcula a soma e a média
soma = sum(elementos)
media = soma / len(elementos)

# Imprime os resultados
print(f"Lista elementos: {elementos}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media}")