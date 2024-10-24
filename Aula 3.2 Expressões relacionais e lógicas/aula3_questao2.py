#2) Dando continuidade à questão anterior, 
#um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). 
#Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, 
#mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

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

pode_entrar = idade_juliana >= 18 or idade_cris >= 18

#saída
print(pode_entrar)