valores = [] # Criando uma lista vazia

for item in range(10, 14):
    valores.append(item)
print(valores)

# Preenchendo uma lista com dados dinâmico
valores2 = []
while True:
    num = int(input("Informe uma valor númerico qualquer - zero para encerra: "))
    
    if num == 0:
        break # Encerrar o Sistema
    else:
        valores2.append(num)
print("\nPrograma encerrado \n")
print(valores2)        
    
    