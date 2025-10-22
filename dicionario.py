agenda = {"Maria": 1234, "Pedro": 4321, "Joana": 9876}
contato = {"nome": "Claudio", "Idade":45}

print(type(agenda))

print(agenda)
print("_"*40)
print(agenda["Maria"])# Mostra o conteúdo da chave
print(f"Nome: {contato['nome']} Idade: {contato['Idade']}")


# Inserindo dados na agendas
# Forma 01

agenda["José"] = 1145
print(agenda)

# Forma 02
# update pode inserir um novo valor ou alterar um já existente

agenda.update({"Claudia": 2222})
print(agenda)

agenda.update({"Joana": 3333})
print(agenda)

# Excluindo dados da agenda
# Forma 01

agenda.pop("Pedro")
print(agenda)


# forma 02

del agenda["Maria"]
print(agenda)