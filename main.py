def main():
    programa_rodando = True
    while programa_rodando:
        print("\n===== BIBLIOTECA DO SILVA =====")
        print("1 - Cadastrar livro")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("Você escolheu cadastrar (ainda vamos implementar)")
        elif opcao == "2":
            print("Saindo... até mais!")
            programa_rodando = False
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
         