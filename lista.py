# Criando uma lista
numeros = [3, 5, 10, 14]

print(numeros)

numeros[2] = 15 # Alterando o valor do índice 2

#Exibir todos os números

for item in numeros:
    print(item)
    
# Incerindo valores na lista

numeros.append(23)

print(numeros)

# Adicionando em qualquer lugar

numeros.insert(2, 90) # iremos incerir o valor 90 no índice 2

print(numeros)

# removendo item da lista

numeros.pop() # Removendo item do final da lista
print(numeros)
    
    