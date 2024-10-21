#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível 
#de notas necessárias para pagar aquele valor. 
#As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 

#Entrada:
#576

#Saída:
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00

#Leitura de dados (entrada)
valor = int(input('Digite o valor: '))
# 576

#### Começar da maior nota (quantas notas?)
notas_100 = int(valor // 100) # 576 / 100 = 5

#### Atualizar quanto falta depois da maior nota
valor = valor % 100 # 576 - 5 * 100  # 76 

notas_50 = valor // 50 # 76 // 50 = 1
valor = valor % 50 # volor - 50 * notas_50 # 26

notas_20 = valor // 20 # 26 // 20 = 1
valor = valor % 20          # 6

notas_10 = valor // 10 # 6 // 10 = 0
valor = valor % 10          # 6

notas_5 = valor // 5 # 6 // 5 = 1
valor = valor % 5        # 1

notas_2 = valor // 2 # 1 // 2 = 0
valor = valor % 2       # 1

notas_1 = valor 

#Imprimindo o resultado (saída)
print (f'{notas_100} nota(s) de 100')
print (f'{notas_50} nota(s) de 50')
print (f'{notas_20} nota(s) de 20')
print (f'{notas_10} nota(s) de 10')
print (f'{notas_5} nota(s) de 5')
print (f'{notas_2} nota(s) de 2')
print (f'{notas_1} nota(s) de 1')