public class Pessoa {
  private static int contadorID = 1;
  private int id;
  private String nome;
  private String musica;

  public Pessoa(String nome, String musica) {
    this.id = contadorID++;
    this.nome = nome;
    this.musica = musica;
  }

  public int getID() { return id; }
  public String getNome() { return nome; }
  public String getMusica() { return Musica; }
  
  public void setMusica (String setMusica) { 
    this.musica = musica; 
  }
  
  @Override 
  public String toString() { 
    return "ID: " + id + " | Nome: " + nome + " | Música: " + musica; 
  }
}
