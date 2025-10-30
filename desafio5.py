# Sistema de Biblioteca Pessoal

biblioteca = {}

def adicionar_livro():
    nome = input("Digite o nome do livro: ").strip()
    if nome in biblioteca:
        print("⚠️ Este livro já está cadastrado!")
    else:
        try:
            paginas = int(input("Digite o número de páginas: "))
            biblioteca[nome] = paginas
            print(f"📚 Livro '{nome}' adicionado com {paginas} páginas.")
        except ValueError:
            print("❌ Número de páginas inválido! Use apenas números.")

def consultar_livro():
    nome = input("Digite o nome do livro: ").strip()
    if nome in biblioteca:
        print(f"📖 O livro '{nome}' tem {biblioteca[nome]} páginas.")
    else:
        print("❌ Livro não encontrado.")

def atualizar_paginas():
    nome = input("Digite o nome do livro que deseja atualizar: ").strip()
    if nome in biblioteca:
        try:
            novas_paginas = int(input("Digite o novo número de páginas: "))
            biblioteca[nome] = novas_paginas
            print(f"✅ Número de páginas do livro '{nome}' atualizado para {novas_paginas}.")
        except ValueError:
            print("❌ Número inválido.")
    else:
        print("❌ Livro não encontrado.")

def remover_livro():
    nome = input("Digite o nome do livro que deseja remover: ").strip()
    if nome in biblioteca:
        del biblioteca[nome]
        print(f"🗑️ Livro '{nome}' removido com sucesso.")
    else:
        print("❌ Livro não encontrado.")

def listar_livros():
    if biblioteca:
        print("\n📚 Lista de Livros Cadastrados:")
        for nome, paginas in biblioteca.items():
            print(f"  - {nome}: {paginas} páginas")
    else:
        print("📭 Nenhum livro cadastrado.")

def contar_livros():
    print(f"📘 Total de livros cadastrados: {len(biblioteca)}")

# --- Menu Principal ---
while True:
    print("\n=== SISTEMA DE BIBLIOTECA PESSOAL ===")
    print("1. Adicionar livro")
    print("2. Consultar livro")
    print("3. Atualizar páginas")
    print("4. Remover livro")
    print("5. Listar todos os livros")
    print("6. Contar livros")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        atualizar_paginas()
    elif opcao == "4":
        remover_livro()
    elif opcao == "5":
        listar_livros()
    elif opcao == "6":
        contar_livros()
    elif opcao == "7":
        print("👋 Encerrando o sistema. Até mais!")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")
