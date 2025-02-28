# Mapeamento de códigos de emojis para emojis Unicode
emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

# Exibe a lista de emojis disponíveis
print("Emojis disponíveis:\n")
for codigo, simbolo in emojis_disponiveis.items():
    print(f"{simbolo} - {codigo}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

# Converte a frase substituindo os códigos pelos emojis correspondentes
frase_emojizada = frase_codificada
for codigo, simbolo in emojis_disponiveis.items():
    frase_emojizada = frase_emojizada.replace(codigo, simbolo)

# Exibe a frase emojizada
print("\nFrase emojizada:\n", frase_emojizada)
