impares = []

print("Digite números inteiros (0 para encerrar):")

while True:
    try:
        numero = int(input("Número: "))
        
        if numero == 0:
            break
        
        if numero % 2 != 0:
            impares.append(numero)
            print(f"Ímpar: {numero}")
            
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print(f"\nNúmeros ímpares digitados: {impares}")
print("Programa encerrado.")