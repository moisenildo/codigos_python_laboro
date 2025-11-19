# Trabalhando com o modo:
# 'a' -> (append) adiciona conteúdo no final do arquivo

#Abrindo o arquivo em modo de escrita
arquivo = open("frutas.txt", "a")
arquivo.write("Goiba\n")
arquivo.write("Jambo\n")
arquivo.write("Pitanga\n")
arquivo.write("Pitomba\n")



arquivo.close()