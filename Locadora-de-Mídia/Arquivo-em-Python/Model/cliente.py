# models/cliente.py
class Cliente:
    def __init__(self, id, nome, documento, email):
        self.id = id
        self.nome = nome
        self.documento = documento
        self.email = email
        self.ativo = True

    def desativar(self):
        self.ativo = False
