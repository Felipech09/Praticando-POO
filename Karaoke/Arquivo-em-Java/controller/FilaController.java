import java.util.Queue; 
import java.util.LinkedList; 

public class FilaController { 
  private Queue<Pessoa> fila; 
}

  public FilaController() { 
    fila = new LinkedList<>();
  }

  // adicionar
public void adicionarPessoa(String nome, String musica) { 
  Pessoa p = new Pessoa(nome, musica); 
  fila.add(p); 
  System.out.println("Pessoa adicionada à fila!"); 
}

  // remover
  public void removerPessoa(int id) { 
    boolean removido = fila.removeIf(p -> p.getId() == id); 
    if (removido) { 
      System.out.println("Pessoa removida da fila.");
      } else { 
      System.out.println("ID não encontrado."); 
    } 
  }

public void aletararMusica(int id, String novaMusica) {
  for (Pessoa p : fila) {
    if (p.getId() == id) {
      p.setMusica(novaMusica);
      System.out.println("Música alterada com sucesso!");
      return;
    }
  }
  System.out.println("ID não encontrado");
}

public void chamarProxima(){
  Pessoa p = fila.poll();
  if (p != null) {
    System.out.println("Chamando agora: " + p.getNome() + " para cantar [" + p.getMusica() + "]);
  } else {
    System.out.printon ("A fila está vazia!");
  }
}

public void mostrarFila(){
  if (fila.isempty()){
    System.out.println("Fila vazia!");
  } else {
    System.out.println (" \n --- A fila está organizada da seguinte maneira: --- \n");
    fila.forEach(System.out: :println);
  }
}
