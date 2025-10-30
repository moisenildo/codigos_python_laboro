biblioteca = {} # Inicializando um dicionario

while True:
    print("\n====MINHA BIBLIOTECA PESSOAL====\n")
    print("1 - Adicionar livro")
    print("2 - Consultar livro")
    print("3 - Atualizar páginas")
    print("4 - Remover livro")
    print("5 - Listar todos os livros")
    print("6 - Contar livros")
    print("7 - Sair")
    resposta = int(input("Qaul a sua escolha: "))
    
    if resposta == 1:
        try:
            nome = input("Qual o nome do livro: ")
            biblioteca[nome] = input(f"Qual o número do livro {nome}: ")
            
            print("Livro inserido com sucesso!")
            print(biblioteca)
            
        except Exception:
            print("Operação invalida. Contato não salvo. ")
    
    
    
    
    
    
    
    elif resposta == 7:
        print("Sistema Encerrado")
        
        break  