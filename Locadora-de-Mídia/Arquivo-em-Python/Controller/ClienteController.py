from models.cliente import Cliente

class ClienteController:
    def __init__(self):
        self.clientes = []
        self.next_id = 1

    def criar(self, nome, documento, email):
        cliente = Cliente(self.next_id, nome, documento, email)
        self.clientes.append(cliente)
        self.next_id += 1
        return cliente

    def listar(self):
        return self.clientes
