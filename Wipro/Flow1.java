import java.util.*;
public class Flow1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        if (n1==0){
            System.out.println("Zero");
        }
        else if(n1>0){
            System.out.println("Positive");
        }
        else{
            System.out.println("negative");
        }
        sc.close();
    }
}