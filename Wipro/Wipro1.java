import java.util.*;
public class Wipro1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("hello all");
        String first = sc.next();
        String second = sc.next();
        if ("Wipro".equals(first) && "Bangalore".equals(second)) {
            System.out.println("Wipro Technologies Bangalore.");
        } else if ("ABC".equals(first) && "Mumbai".equals(second)) {
            System.out.println("ABC Technologies Mumbai.");
        }
        sc.close();
    }
}