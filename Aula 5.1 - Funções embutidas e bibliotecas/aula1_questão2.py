import random
import math

# Peça ao usuário o valor de n
n = int(input("Digite a quantidade de números inteiros aleatórios (n): "))
soma = 0

for i in range(n):
    valor = random.randint(0, 100)
    print(valor)
    soma += valor

    print(soma)
    print(f"A raiz quadrada da soma é: {math.sqrt(soma)}")


