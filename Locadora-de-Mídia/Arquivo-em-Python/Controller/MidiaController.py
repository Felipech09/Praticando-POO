from models.midia import Midia

class MidiaController:
    def __init__(self):
        self.midias = []
        self.next_id = 1

    def criar(self, titulo, tipo, classificacao, estoque_total, preco_base):
        midia = Midia(self.next_id, titulo, tipo, classificacao, estoque_total, preco_base)
        self.midias.append(midia)
        self.next_id += 1
        return midia

    def listar(self):
        return self.midias
