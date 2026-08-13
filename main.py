def cadastrar_livro(livros):
    print("\n=== Cadastro do novo livro ===")
    titulo = input("Título do livro: ").strip()
    ano = input("Ano de publicação: ").strip()
    autor = input("Nome do autor: ").strip()
    isbn = input("Código/ISBN: ").strip()

    novo_livro = {
        "Titulo": titulo,
        "Ano": ano,
        "Autor": autor,
        "ISBN": isbn,
    }
    
    livros.append(novo_livro)
    print(f"Livro '{titulo}' foi cadastrado com sucesso 👍🏻")
    return livros


def main():
    programa_rodando = True
    livros = []  # Lista para armazenar os livros cadastrados

    while programa_rodando:
        print("\n===== BIBLIOTECA DO SILVA =====")
        print("1 - Cadastrar livro")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            livros = cadastrar_livro(livros)
        elif opcao == "2":
            print("Saindo... até mais!")
            programa_rodando = False
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()