from Model.fila_karaoke import FilaKaraoke
from Model.pessoa import Pessoa

class FilaController:
    def __init__(self):
        self.fila_karaoke = FilaKaraoke()

    def adicionar_pessoa(self, nome, musica):
        p = Pessoa(nome, musica)
        self.fila_karaoke.adicionar_pessoa(p)
        print("Pessoa adicionada à fila!")

    def remover_pessoa(self, id_busca):
        removido = self.fila_karaoke.remover_pessoa(id_busca)
        if removido:
            print("Pessoa removida da fila.")
        else:
            print("ID não encontrado.")

    def alterar_musica(self, id_busca, nova_musica):
        alterado = self.fila_karaoke.alterar_musica(id_busca, nova_musica)
        if alterado:
            print("Música alterada com sucesso!")
        else:
            print("ID não encontrado")

    def chamar_proxima(self):
        p = self.fila_karaoke.chamar_proxima()
        if p:
            print(f"Chamando agora: {p.get_nome()} para cantar '{p.get_musica()}'")
        else:
            print("A fila está vazia.")

    def mostrar_fila(self):
        if self.fila_karaoke.is_empty():
            print("Fila vazia")
        else: 
            print("\nA fila está organizada da seguinte maneira:")
            for p in self.fila_karaoke.get_fila():
                print(p)