#2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. 
#O programa deve imprimir uma mensagem correspondente à classificação do filme:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

filme = int(input("Em uma escala de 1 a 5, qual a sua avaliação para o filme, sendo 1 ruim e 5 excelente? "))

#Validando a avaliaçõo
if  filme == 1:
    print("Ruim")
elif filme == 2:
    print("Regular")
elif filme == 3:
    print("Bom!")
elif filme == 4:
    print("Muito bom!")
elif filme == 5:
    print("Excelente")
else:
    print("avaliação improcedente")



