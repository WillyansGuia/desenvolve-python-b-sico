#leia n1, n2, n3
#n = (n1 + n2 + n3)/3
#m>=60
#se sim imprima " aprovado"
#se não 
#mm>=40 se sim imprima " Recuperação"
#se não imprima "Reprovado"
#caso contrario imprima "Fim"

#variável de controle de laço
n = int(input())

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
cont = 0
#Cálculo da média
n = (n1 + n2 + n3)/3


while cont < n:
    cont += 1
    if n >= 60:
        print("Aprovado")
    elif n >= 40:
        print("Recuperação")
    else:
        print("Reprovado")

    if n1 == -1:
        print("Fim")
        break