import java.util.Scanner;

public class Menu {
    public void iniciar() {
        Scanner sc = new Scanner(System.in);
        FilaController controller = new FilaController();

        int opcao;
        do {
            System.out.println("\n🎤 ========= KARAOKÊ ========= 🎤");
            System.out.println("1 - Adicionar pessoa");
            System.out.println("2 - Remover pessoa");
            System.out.println("3 - Alterar música");
            System.out.println("4 - Chamar próxima pessoa");
            System.out.println("5 - Mostrar fila");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {
                case 1:
                    System.out.print("Nome: ");
                    String nome = sc.nextLine();
                    System.out.print("Música: ");
                    String musica = sc.nextLine();
                    controller.adicionarPessoa(nome, musica);
                    break;
                case 2:
                    System.out.print("ID para remover: ");
                    int idRemover = sc.nextInt();
                    controller.removerPessoa(idRemover);
                    break;
                case 3:
                    System.out.print("ID para alterar música: ");
                    int idAlterar = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Nova música: ");
                    String novaMusica = sc.nextLine();
                    controller.alterarMusica(idAlterar, novaMusica);
                    break;
                case 4:
                    controller.chamarProxima();
                    break;
                case 5:
                    controller.mostrarFila();
                    break;
                case 0:
                    System.out.println("Encerrando sistema...");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        } while (opcao != 0);

        sc.close();
    }
}
