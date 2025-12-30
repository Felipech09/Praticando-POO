import java.util.Queue;
import java.util.LinkedList;

public class FilaController {
    private FilaKaraoke filaKaraoke;

    public FilaController() {
        this.filaKaraoke = new FilaKaraoke();
    }

    public void adicionarPessoa(String nome, String musica) {
        Pessoa p = new Pessoa(nome, musica);
        filaKaraoke.adicionarPessoa(p);
        System.out.println("Pessoa adicionada à fila!");
    }

    public void removerPessoa(int id) {
        boolean removido = filaKaraoke.removerPessoa(id);
        if (removido) {
            System.out.println("Pessoa removida da fila.");
        } else {
            System.out.println("ID não encontrado.");
        }
    }

    public void alterarMusica(int id, String novaMusica) {
        boolean alterado = filaKaraoke.alterarMusica(id, novaMusica);
        if (alterado) {
            System.out.println("Música alterada com sucesso!");
        } else {
            System.out.println("ID não encontrado.");
        }
    }

    public void chamarProxima() {
        Pessoa p = filaKaraoke.chamarProxima();
        if (p != null) {
            System.out.println("Chamando agora: " + p.getNome() + " para cantar '" + p.getMusica() + "'");
        } else {
            System.out.println("A fila está vazia!");
        }
    }

    public void mostrarFila() {
        if (filaKaraoke.isEmpty()) {
            System.out.println("Fila vazia!");
        } else {
            System.out.println("\n--- A fila está organizada da seguinte maneira: ---");
            for (Pessoa p : filaKaraoke.getFila()) {
                System.out.println(p);
            }
        }
    }
}
