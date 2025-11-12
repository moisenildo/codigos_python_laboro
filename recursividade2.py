# Função que irá somar valores
def soma_ate(n):
    # caso base se n for igual 1 devolve 1
    print(f"Entrando na soma_ate({n})")
    if n == 1:
        print("-> caso base! retornando 1")
        return 1
    resultado = n + soma_ate(n-1)
    print(f"<- Retornando {n} + .... = {resultado}")
    
    # Caso recursivo: n + soma dos anteriores.
    return resultado 

# Chamando a função - exemplo

print(soma_ate(3))

    