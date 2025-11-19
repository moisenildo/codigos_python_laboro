# Vamos abrir um arquivo

'''
r -> modo de leitura
w -> escrita / criação

'''
# abrindo um arquivo em modo leitura

arquivo = open("frutas.txt", "r")

# verificando se um arquivo pode ser lido

print(arquivo.readable)

#print(arquivo.read())# Lendo conteudo de um arquivo

#Lendo apenas uma linha do arquivo
#print(arquivo.readline())

resultado = arquivo.readlines()
print(resultado[3])



arquivo.close()# fechando arquivo