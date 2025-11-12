# Contagem com recursividade

def contagem(num):
    if num >= 1:
        print(num)
        num = num - 1
        contagem(num)   
# Chamando a função
contagem(10)
        