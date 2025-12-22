import java.util.LinkedList;
import java.util.Queue;

public class FilaKaraoke {
    private Queue<Pessoa> fila;

    public FilaKaraoke() {
        fila = new LinkedList<>();
    }

    public void adicionarPessoa(Pessoa pessoa) {
        fila.add(pessoa);
    }

    public boolean removerPessoa(int id) {
        return fila.removeIf(p -> p.getId() == id);
    }

    public boolean alterarMusica(int id, String novaMusica) {
        for (Pessoa p : fila) {
            if (p.getId() == id) {
                p.setMusica(novaMusica);
                return true;
            }
        }
        return false;
    }

    public Pessoa chamarProxima() {
        return fila.poll();
    }

    public boolean isEmpty() {
        return fila.isEmpty();
    }

    public Queue<Pessoa> getFila() {
        return fila;
    }
}
