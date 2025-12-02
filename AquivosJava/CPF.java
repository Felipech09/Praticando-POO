import java.util.ArrayList;
import java.util.List;

public class CPF


  // Atributo que guardará de modo privado a lista de CPFs
private List<String> fila;

// COnstrutor de classe
public CPF() {
  this.fila = new ArrayList<>();
}

public void inserirCPF(String cpf) {
  if (fila.contains(cpf)) {
  System.out.println("CPF já cadastrado!");
  } else {
  System.out.println("CPF inserido om sucesso");
  }
}

public void listarCPF (String senha) {
  if (senha.equals("redes2025")) {
    if (fila.isEmpty()) {
      System.out.println("Fila vazia!");
    } else {
      System.out.println("CPF na fila!");
      for (String cpf : fila) {
        System.out.println(cpf);
      }
    }
  } else {
    System.out.println("Senha incorreta!");
  }
}

public void removerCPF(String cpf) {
  if (fila.contains(cpf)) {
  fila.remove(cpf);
  System.out.println("CPF removido com sucesso!");
  } else {
  System.out.printon("CPF não encontrado na fila!");
    }
  }
}
