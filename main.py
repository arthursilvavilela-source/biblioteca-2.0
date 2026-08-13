import csv


def carregar_livros():
    livros = []
    try:
        with open("livros.csv", mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        pass
    return livros
def salvar_todos_os_livros(livros):
   with open("livros.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    colunas = ["Titulo", "Ano", "Autor", "ISBN"]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(livros)


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

    # Lógica para salvar a linha no arquivo CSV
    arquivo_existe = False
    try:
        with open("livros.csv", mode="r", encoding="utf-8") as f:
            if f.read(1):
                arquivo_existe = True
    except FileNotFoundError:
        arquivo_existe = False

    with open("livros.csv", mode="a", newline="", encoding="utf-8") as arquivo:
        colunas = ["Titulo", "Ano", "Autor", "ISBN"]
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)

        if not arquivo_existe:
            escritor.writeheader()

        escritor.writerow(novo_livro)

    print(f"Livro '{titulo}' foi cadastrado com sucesso 👍🏻 ")
    return livros


def listar_livros(livros):
    print("\n=== Lista de livros cadastrados ===")

    if len(livros) == 0:
        print("Nenhum livro cadastrado até o momento.")
        return
    for indice, livro in enumerate(livros, start=1):
        print(f"\n  Livro #{indice}")
        print(f" Título: {livro['Titulo']}")
        print(f" Autor:  {livro['Autor']}")
        print(f" Ano:    {livro['Ano']}")
        print(f" ISBN:   {livro['ISBN']}")
def buscar_livro(livros):
    print("\n=== Buscar livor por Titulos===")
    
    if len(livros) == 0:
        print("Nenhum livro cadastrado para pesquisa.")
        return
    termo_busca = input("Digite o titulo (ou parte dele): ").strip
    encontrado = False
    if termo_busca in livro["titulo"].lower():
            print(f"\n Livro encontrado 😃")
            print(f" Título: {livro['Titulo']}")
            print(f" Autor:  {livro['Autor']}")
            print(f" Ano:    {livro['Ano']}")
            print(f" ISBN:   {livro['ISBN']}")
            encontrado = True
            if not encontrado:
                print(f"\nNenhum livro com esse nome{termo_busca} foi encontrado")
def remover_livro(livros):
    print("\n===Remover livro===")
    if len(livros) == 0:
        print("Nenhum livro cadastrado para remover.")
        return livros
    for indice, livro in enumerate(livros, start=1):
        print(f"{indice} - {livro['Titulo']} ({livro['Autor']})")
    escolha = input("\nDigite o número do livro que deseja apagar (ou 0 para cancelar): ").strip()
    if escolha.isdigit():
        numero = int(escolha)
        if 1 <= numero <= len(livros):
            livro_removido = livros.pop(numero - 1)  # Apaga o livro escolhido
            salvar_todos_os_livros(livros)          # Atualiza o arquivo CSV
            print(f"Livro '{livro_removido['Titulo']}' removido com sucesso!")
        elif numero == 0:
            print("Operação cancelada.")
        else:
            print("Número de livro inválido.")
    else:
        print("Por favor, digite apenas números.")

    return livros

def main():
    programa_rodando = True
    livros = carregar_livros()

    while programa_rodando:
        print("\n===== BIBLIOTECA DO SILVA =====")
        print("1 - Cadastrar livro")
        print("2 - Listar todos os livros")
        print("3 - Buscar livro por título")
        print("4 - Remover livro")  # <- Opção nova!
        print("5 - Sair")           # <- Sair virou 5
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            livros = cadastrar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            buscar_livro(livros)
        elif opcao == "4":
            livros = remover_livro(livros)  # <- Chama a remoção!
        elif opcao == "5":
            print("Saindo... até mais!")
            programa_rodando = False
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()