import java.util.*;

public class Flow3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().trim(); 
        if (input.isEmpty()) {
            System.out.print("No Values");
        } else {
            System.out.println(input);
        }
        sc.close();
    }
}