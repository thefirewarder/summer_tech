public class Card{
    public int value;
    public String suit;
    public int getValue(){
        return this.value;
    }
    public String getSuit(){
        return this.suit;
    }
    public Card(int value, String suit){
        this.value = value;
        this.suit = suit;
    }

    public String toString()
    {   
       String valueString = value+"";
       if(value==11){
        valueString = "Jack";
       }
       else if(value==12){
       valueString = "Queen";
       }
       else if(value == 13){
        valueString = "King";
       }
       else if(value == 1){
        valueString = "Ace";
       }
       return valueString;
    }
}