import java.util.*;
public class Flow4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char one = sc.next().charAt(0);
        char two = sc.next().charAt(0);
        if((int)one<(int)two){
            System.out.printf("%c,%c",one,two);
        }
        else{
            System.out.printf("%c,%c",two,one);
        }
    }
}