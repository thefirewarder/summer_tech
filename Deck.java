public class Deck {
    private Card[] stack;
    public Deck(){
        stack=new Card[52];
        int count = 1;
        for(int i = 1; i <= 13; i++){
          stack[i] = new Card(i, "Spades");
          count++;
          stack[i] = new Card(i, "Clubs");
          count++;
          stack[i] = new Card(i, "Hearts");
          count++;
          stack[i] = new Card(i, "Diamonds");
          count++;
        }
    }
}

