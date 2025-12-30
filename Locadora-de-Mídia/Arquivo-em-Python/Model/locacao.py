from datetime import datetime, timedelta

class Locacao:
    def __init__(self, id, cliente, midia, dias):
        self.id = id
        self.cliente = cliente
        self.midia = midia
        self.data_locacao = datetime.now()
        self.data_prevista = self.data_locacao + timedelta(days=dias)
        self.data_devolucao = None
        self.valor_total = 0.0
        self.status = "ABERTA"

    def encerrar(self):
        self.data_devolucao = datetime.now()
        self.status = "ENCERRADA"
        self.midia.devolver()
