alimentos = {"Arroz":5.99, "Café":14, "Feijão":7.69}

""""
Dicionário
Chave: valor -> item

Chave - key
Valor - value
item - item

"""

print(alimentos)

# acessando apenas as chaves

for chave in alimentos.keys():
    print(chave)

# acessando apenas os Valores

for valor in alimentos.values():
    print(valor)

# acessando tanto chave quanto valor

for chave, valor in alimentos.items():
    print(f"{chave} : {valor}")    
        