import java.io.*;
import java.util.Stack;
import java.util.Scanner;

public class compute {
    public static void compile(String input){
        int[] memory = new int[999];
        Stack<Integer> stack = new Stack<>();
        String[] words = input.split(" ");
        for(int i = 0; i < words.length; i++){
            if(words[i].equals("out")){
                String[] words2 = words[i+1].split("-");
                for(int j = 0; j < words2.length; j++){
                    System.out.print(words2[j]+" ");
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            File file = new File("input.txt");
            Scanner scanner = new Scanner(file);

            StringBuilder inputBuilder = new StringBuilder();
            while (scanner.hasNextLine()) {
                inputBuilder.append(scanner.nextLine()).append(" ");
            }

            scanner.close();

            compile(inputBuilder.toString().trim());

        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }
}
