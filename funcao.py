# Função - Modo 1 sem parametro e sem retorno

def menu ():
    print("---MENU DO SISTEMA ---")
    print("1 - CONSULTA")
    print("2 - INSERIR")
    print("3 - EXCLUIR")
# CHAMANDO FUNÇÃO
menu()    

# FUNÇÃO MODO 2 com parametro e sem retorno

def somar (num1,num2):
    print(f"A soma é {num1 + num2}")

# chamando a função soma

somar(4,5)


# Função - Modo 3 - sem parametro com retorno
def dobro():
    valor = int(input("Informe um valor numérico: "))
    
    return valor * 2

# Chamando a função
print(f"O dobro é {dobro() + 10}")

# função - modo 4 - com parametro e com retorno

def triplo(valor):
    resposta = valor * 3
    
    return resposta

# Chamando a função
print(f"O triplo do valor e {triplo(8)}")

# Chamando a função com valor dinamico

numero = int(input("informe um valor:"))
print(f"O triplo do valor é {triplo(numero)}")



    

 
       
    
    
