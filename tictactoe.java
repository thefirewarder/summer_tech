import java.util.Scanner;
public class tictactoe{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        printBoard();
    }
}
public static int[][] printBoard(){
    for(int i = 0; i < 3; i++){
        for(int j = 0; i < 3; i++){
            board[i][j]='-';
        }
    }
}