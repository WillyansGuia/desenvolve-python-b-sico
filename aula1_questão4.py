from datetime import datetime

# Obtém a data e hora atual
agora = datetime.now()

# Formata e exibe a data
print("Data:", agora.strftime("%d/%m/%Y"))

# Formata e exibe a hora
print("Hora:", agora.strftime("%H:%M"))
