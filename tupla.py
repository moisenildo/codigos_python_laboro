# Tupla é Conjunto de dados 
# Criando uma tupla
# frutas = tuple() "Tipo de criar tupla".

frutas = ("Banana", "Uva", "Morango", "Açerola")

#print(type(frutas))

print(frutas)
frutas[2] = "Manga" # aqui teremos um erro

print(frutas[2]) # Busca com indice

# Exibir todas as frutas

for item in frutas:
    print(item)
