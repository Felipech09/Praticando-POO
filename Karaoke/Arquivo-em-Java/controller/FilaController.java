import java.util.Queue; 
import java.util.LinkedList; 

public class FilaController { 
  private Queue<Pessoa> fila; 
  private int totalCantaram;
  
  public FilaController() { 
    fila = new LinkedList<>(); totalCantaram = 0; 
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
