# Trabalhando com os modos:
'''
w -> escrevendo(substitui) / cria arquivl

'''

arquivo = open("frutas.tct", "w")
print(arquivo.write())
arquivo.write("MAracuja\n")
arquivo.write("Acerola\n")
arquivo.write("Manga\n")

# verificando se um arquivo pode se escrito


arquivo.close()

# Criando outro arquivo
arquivo = open("Verdula.txt", "w")
arquivo.write("Batata\n")
arquivo.write("Csenora\n")
arquivo.write("Maxixe\n")
arquivo.write("Quiabo\n")


arquivo.writelines({"Macaxeira\n", "Beterraba\n"})


arquivo.close()