class LocacaoView:
    @staticmethod
    def mostrar(locacao):
        print(f"Locação [{locacao.id}] Cliente {locacao.cliente.nome} - Mídia {locacao.midia.titulo} - "
              f"Status: {locacao.status}")
