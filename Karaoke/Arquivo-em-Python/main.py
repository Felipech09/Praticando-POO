from Controller.fila_controller import FilaController

def main():
    controller = FilaController()

    while True:
        print("\n ========= KARAOKÊ =========")
        print("1 - Adicionar pessoa")
        print("2 - Remover pessoa")
        print("3 - Alterar música")
        print("4 - Chamar próxima pessoa")
        print("5 - Mostrar fila")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            musica = input("Música: ")
            controller.adicionar_pessoa(nome, musica)
        elif opcao == "2":
            try:
                id_rem = int(input("ID para remover: "))
                controller.remover_pessoa(id_rem)
            except ValueError:
                print("Por favor, digite um ID numérico válido.")
        elif opcao == "3":
            try:
                id_alt = int(input("ID para alterar a música: "))
                nova_musica = input("Nova música: ")
                controller.alterar_musica(id_alt, nova_musica)
            except ValueError:
                print("Por favor, digite um ID numérico válido.")
        elif opcao == "4":
            controller.chamar_proxima()
        elif opcao == "5":
            controller.mostrar_fila()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else: 
            print("Opção inválida!")

if __name__ == "__main__":
    main()