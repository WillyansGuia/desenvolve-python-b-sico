#1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
#Escreva um programa que solicite as idades de Juliana e Cris 
#e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.

#entrada de dados

#idade de Juliana
idade_juliana = int(input())
#idade de Cris
idade_cris = int(input())

#Processamento
#True se ambos forem maiores de idade
#<exp1> Juliana é maior de idade
#<exp2> Cris é maior de idade
#11<exp1> and <exp2>
#False em qualquer outro caso

pode_entrar = idade_juliana > 17  and idade_cris > 17


#saída
print(pode_entrar)

