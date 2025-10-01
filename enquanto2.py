# Forma condicional 1

senha = 1234 # Estamos inicializando a variável

"""
while senha != 12345:
    senha = int(input(" Informe a sua senha: "))
    print("Obrigado por usar a nossa senha")
"""    
# Forma Condicional 2

tentativas = 3
while True:
    senha = input("Informe a sua senha: ")
       
    if senha == "aluno2" and tentativas > 0:
        print("Parabens vc acertou a senha")
        break # Este comando irá incerrar o while. 
    if tentativas > 0:
        tentativas -= 1 # Está diminuindo aas tentativas
        
    if tentativas == 0: 
        print("Sem tentativas, só lamento")
        break    
    
    
