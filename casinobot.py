import random
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts","Diamonds","Spades","Clubs"]
        ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for i in range(13):
            rank = ranks[i]
            for j in range(4):
                suit = suits[j]
                self.cards.append(rank+" of "+suit)
    def shuffle(self):
        for _ in range(10):
            for j in range(52):
                switcher = random.randint(0,51)
                temp = self.cards[j]
                self.cards[j] = self.cards[switcher]
                self.cards[switcher] = temp
    def __str__(self):
        return "\n".join(self.cards)
p_hand = []
b_hand = []
deck = Deck()
def deal_hand():
    global p_hand
    global b_hand
    deck = Deck()
    deck.shuffle()
    for _ in range(2):
        p_hand.append(deck.cards[0])
        deck.cards.pop(0)
        b_hand.append(deck.cards[0])
        deck.cards.pop(0)
balance = 100
running = True
while(running):
    deal_hand()
    bet = int(input("What would you like to bet on this round?"))
    while bet > balance:
        bet = int(input("You only have ",balance,". Now, What would you like to bet on this round?"))
    balance -= bet
    print("Great! You now have $",balance,"!")
    print("The hands have been dealt. Your cards are the "+p_hand[0]+" and the "+p_hand[1])
    status = input("Would you like to hit or stand?")
    while(status != "hit" and status != "stand"):
        status = input("Let's try again. Would you like to hit or stand?")
    if status == "hit":
        p_hand.append(deck.cards[0])
        deck.cards.pop(0)
        hand_value = 0
        for card in p_hand:
            if card.startswith("2"):
                hand_value += 2
            elif card.startswith("3"):
                hand_value += 3
            elif card.startswith("4"):
                hand_value += 4
            elif card.startswith("5"):
                hand_value += 5
            elif card.startswith("6"):
                hand_value += 6
            elif card.startswith("7"):
                hand_value += 7
            elif card.startswith("8"):
                hand_value += 8
            elif card.startswith("9"):
                hand_value += 9
            elif card.startswith("10") or card.startswith("Jack") or card.startswith("Queen") or card.startswith("King"):
                hand_value += 10
            elif card.startswith("Ace"):
                if 10 <= hand_value <= 21:
                    hand_value += 11
                elif hand_value < 10:
                    hand_value += 1
                elif balance <= 0:
                    print("You busted! The bot wins the whole game!")
                    running = False
    elif status == "stand":






