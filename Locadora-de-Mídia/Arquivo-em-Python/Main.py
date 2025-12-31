from controllers.cliente_controller import ClienteController
from controllers.midia_controller import MidiaController
from controllers.locacao_controller import LocacaoController
from views.menu_view import MenuView
from views.cliente_view import ClienteView
from views.midia_view import MidiaView
from views.locacao_view import LocacaoView

def main():
    cliente_ctrl = ClienteController()
    midia_ctrl = MidiaController()
    locacao_ctrl = LocacaoController()

    while True:
        MenuView.mostrar()
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            doc = input("Documento: ")
            email = input("Email: ")
            c = cliente_ctrl.criar(nome, doc, email)
            print(f"Cliente criado: {c.id} - {c.nome}")
        elif op == "2":
            ClienteView.mostrar(cliente_ctrl.listar())
        elif op == "3":
            titulo = input("Título: ")
            tipo = input("Tipo (FILME/SERIE/JOGO): ")
            classif = input("Classificação: ")
            estoque = int(input("Estoque total: "))
            preco = float(input("Preço base: "))
            m = midia_ctrl.criar(titulo, tipo, classif, estoque, preco)
            print(f"Mídia criada: {m.id} - {m.titulo}")
        elif op == "4":
            MidiaView.mostrar(midia_ctrl.listar())
        elif op == "5":
            cliente_id = int(input("ID cliente: "))
            midia_id = int(input("ID mídia: "))
            dias = int(input("Dias de locação: "))
            cliente = next(c for c in cliente_ctrl.listar() if c.id == cliente_id)
            midia = next(m for m in midia_ctrl.listar() if m.id == midia_id)
            loc = locacao_ctrl.abrir(cliente, midia, dias)
            LocacaoView.mostrar(loc)
        elif op == "6":
            locacao_id = int(input("ID locação: "))
            loc = locacao_ctrl.encerrar(locacao_id)
            LocacaoView.mostrar(loc)
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
