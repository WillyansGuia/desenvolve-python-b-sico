#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
# Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais
# e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs
# para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

# Solicita os dois números decimais ao usuário
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta e arredonda para duas casas decimais
diferenca_absoluta = round(abs(primeiro_numero - segundo_numero), 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é: {diferenca_absoluta}")



 