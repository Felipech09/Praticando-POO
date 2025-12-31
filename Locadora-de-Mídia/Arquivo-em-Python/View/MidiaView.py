class MidiaView:
    @staticmethod
    def mostrar(midias):
        for m in midias:
            print(f"[{m.id}] {m.titulo} ({m.tipo}) - Classificação: {m.classificacao} | "
                  f"Disponível: {m.estoque_disponivel}/{m.estoque_total} | R$ {m.preco_base:.2f}")
