public class ticbot {
    public static void main(){
        char[][] board = new char[3][3];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                board[i][j] = '-';
            }
        }
    }
}
