class Pessoa:
    __contador_id = 1

    def __init__(self, nome, musica):
        self.__id = Pessoa.__contador_id
        Pessoa.__contador_id += 1
        self.__nome = nome
        self.__musica = musica

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_musica(self):
        return self.__musica

    def set_musica(self, musica): 
        self.__musica = musica

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Música: {self.__musica}"