class Midia:
    def __init__(self, id, titulo, tipo, classificacao, estoque_total, preco_base):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.classificacao = classificacao
        self.estoque_total = estoque_total
        self.estoque_disponivel = estoque_total
        self.preco_base = preco_base

    def disponivel(self):
        return self.estoque_disponivel > 0

    def reservar(self):
        if not self.disponivel():
            raise ValueError("Sem estoque disponível.")
        self.estoque_disponivel -= 1

    def devolver(self):
        if self.estoque_disponivel < self.estoque_total:
            self.estoque_disponivel += 1
