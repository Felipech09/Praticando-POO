from models.locacao import Locacao

class LocacaoController:
    def __init__(self):
        self.locacoes = []
        self.next_id = 1

    def abrir(self, cliente, midia, dias):
        if not midia.disponivel():
            raise ValueError("Mídia indisponível.")
        midia.reservar()
        locacao = Locacao(self.next_id, cliente, midia, dias)
        self.locacoes.append(locacao)
        self.next_id += 1
        return locacao

    def encerrar(self, locacao_id):
        loc = next((l for l in self.locacoes if l.id == locacao_id), None)
        if not loc or loc.status != "ABERTA":
            raise ValueError("Locação inválida.")
        loc.encerrar()
        return loc
