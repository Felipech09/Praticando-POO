class FilaKaraoke:
    def __init__(self):
        self.__fila = [] 

    def adicionar_pessoa(self, pessoa):
        self.__fila.append(pessoa)

    def remover_pessoa(self, id_busca):
        tamanho_inicial = len(self.__fila)
        self.__fila = [p for p in self.__fila if p.get_id() != id_busca]
        return len(self.__fila) < tamanho_inicial

    def alterar_musica(self, id_busca, nova_musica):
        for p in self.__fila:
            if p.get_id() == id_busca:
                p.set_musica(nova_musica)
                return True
        return False

    def chamar_proxima(self):
        if not self.is_empty():
            return self.__fila.pop(0)
        return False

    def is_empty(self):
        return len(self.__fila) == 0

    def get_fila(self):
        return self.__fila