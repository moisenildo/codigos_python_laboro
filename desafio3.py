valores3 = []
while True:
    print(valores3)
    
    print("Deseja apagar? 1-sim 2-não")
    resposta = int(input("Qual A sua resposta? "))
    
    if len(valores3)<=0:
        print("Lista vazia")
        break
    elif resposta ==1:
        valores3.pop()
    elif resposta == 2:
        break    