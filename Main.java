package ChemChain;

import java.util.Hashtable;
import java.util.Scanner;
import java.util.String;

public class Main {

    private static int eval(char element){
        int evaluate = 1;
        if (evaluate == 1 || evaluate % 8 <= 4){return evaluate;}
        else if (evaluate == 2){return 0;}
        else if (evaluate % 8 >= 5){return evaluate-8;}
        else{return 0;}
    }

    private static char[][] processInput(String process){
        String[] process_convert = process.replaceAll("\\s+","").split("\\+");
        char[][] new_return = new char[process_convert.length][];
        for (int n = 0; n < process_convert.length; n++){new_return[n] = process_convert[n].toCharArray();}

        return new_return;
    }

    private static String input(String request){
        System.out.print("\n"+request);
        Scanner temp = new Scanner(System.in);
        return temp.nextLine();
    }

    public static void main(String[] args){
        String enter = input("Input chemical forumla:\t");
        char[][] formula = processInput(enter);
        for (int n = 0; n < formula.length; n++){System.out.print(String.valueOf(formula[n]));}
    }
}