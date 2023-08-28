import java.util.Scanner;

public class EjemploTryCatch2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Ingrese un número: ");
            int numero = sc.nextInt(); // Intenta leer un entero del usuario

            System.out.println("Número ingresado: " + numero);
        } catch (java.util.InputMismatchException e) {
            System.err.println("Error: Ingrese un número válido.");
        }

        sc.close();
    }
}
