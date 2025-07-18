import java.io.*;
import java.util.HashMap;
import java.util.Scanner;
//Suffixes: ~: Non-variable including consonant start ~~: variable consonant including start ;: non-variable including vowel start ;;: variable including vowel start. When variables are optional in a function, use ~ or ;.
public class compute {

    public static void compile(String input) {
        HashMap<String, String> memory = new HashMap<>();
        String[] words = input.split(" ");

        for (int i = 0; i < words.length; i++) {
            if (words[i].equals("say")&& words[i+1].endsWith("~")) {
                if (i + 1 < words.length) {
                    words[i+1] = words[i+1].substring(0,words[i+1].length()-1);
                    String[] words2 = words[i + 1].split("-");
                    for (String word : words2) {
                        System.out.print(word + " ");
                    }
                    i++; 
                }
            }
            if (words[i].equals("yell")&& words[i+1].endsWith("~")) {
                System.out.println("");
                if (i + 1 < words.length) {
                    words[i+1] = words[i+1].substring(0,words[i+1].length()-1);
                    String[] words2 = words[i + 1].split("-");
                    for (String word : words2) {
                        if(word.equals(words2[0])==false){
                        System.out.print(" "+word);
                        }
                        else{
                        System.out.print(word);

                        }
                    };
                    i++; 
                }
            }

           
            else if (words[i].equals("let")&& words[i+3].endsWith("~~")||words[i].equals("let")&& words[i+5].endsWith("~~")&&words[i+4] instanceof int) {
                words[i+1] = words[i+1].substring(0,words[i+3].length()-2);
                if(words[i+5].endsWith("~~")){
                    String key = words[i+1];

                }
                else{

                }
            }
            
            else if (words[i].equals("parse")&& words[i+1].endsWith("~~")) {
                words[i+1] = words[i+1].substring(0,words[i+1].length()-2);
                if (i + 1 < words.length) {
                    String key = words[i + 1];
                    String value = memory.getOrDefault(key, "undefined");
                    value = value.substring(0,value.length()-2);
                    System.out.print(value);
                    i++;
                }
            }
            else if (words[i].equals("process")&& words[i+1].endsWith("~~")) {
                words[i+1] = words[i+1].substring(0,words[i+1].length()-2);
                System.out.println("");
                if (i + 1 < words.length) {
                    String key = words[i + 1];
                    String value = memory.getOrDefault(key, "undefined");
                    value = value.substring(0,value.length()-2);
                    System.out.print(value);
                    i++;
                }
            }
            else if(words[i].equals("add")&& words[i+1].endsWith(";")){
                 words[i+1] = words[i+1].substring(0,words[i+1].length()-1);
                 if(i+1 < words.length){
                    String[] words2 = words[i+1].split("+");
                    double sum = Double.parseDouble(words2[0]+words2[1]);
                    System.out.print(sum);
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
