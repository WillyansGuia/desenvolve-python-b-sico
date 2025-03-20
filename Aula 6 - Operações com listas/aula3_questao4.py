#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

#Exemplo de interação via terminal (entradas em laranja):


# Recebendo a quantidade de elementos e os valores da lista1
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
print("Digite os", n1, "elementos da lista 1:")
lista1 = []
for i in range(n1):
    elemento = int(input())
    lista1.append(elemento)

# Recebendo a quantidade de elementos e os valores da lista2
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
print("Digite os", n2, "elementos da lista 2:")
lista2 = []
for i in range(n2):
    elemento = int(input())
    lista2.append(elemento)

# Criando a lista intercalada
lista_intercalada = []
i = 0
# Intercalando enquanto houver elementos na lista1
while i < len(lista1):
    lista_intercalada.append(lista1[i])
    if i < len(lista2):  # Só adiciona da lista2 se ainda houver elementos
        lista_intercalada.append(lista2[i])
    i += 1

# Adicionando os elementos remanescentes da lista2, se houver
if len(lista2) > len(lista1):
    lista_intercalada.extend(lista2[len(lista1):])

# Exibindo o resultado
print("\nLista intercalada:", *lista_intercalada)