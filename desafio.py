print("Digite números inteiros (0 para encerrar):")

while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        print("Programa encerrado.")
        break
    
    if numero % 2 != 0:  # Verifica se o número é ímpar
        print(f"Ímpar: {numero}")