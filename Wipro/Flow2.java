import java.util.*;
public class Flow2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int digit = sc.nextInt();
        if (digit%2==0 || digit==0){
            System.out.println("Even");
        }
        else{
            System.out.println("Odd");
        }
        sc.close();

    }
}