package ChemChain;

import java.util.Scanner;
import java.util.String;

public class Main {
    private static char[] processInput(String process){
        return process.replaceAll("\\s+","").toCharArray();
    }
    private static String input(String request){
        System.out.print("\n"+request);
        Scanner temp = new Scanner(System.in);
        return temp.nextLine();
    }
    public static void main(String[] args){
        char[] formula = processInput(input("Input chemical forumla:\t"));
        System.out.println(String.valueOf(formula));
    }
}