class ClienteView:
    @staticmethod
    def mostrar(clientes):
        for c in clientes:
            print(f"[{c.id}] {c.nome} - {c.documento} - {c.email} - {'Ativo' if c.ativo else 'Inativo'}")
