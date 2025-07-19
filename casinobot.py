import random
def get_b_hand_value():
    b_hand_value = 0 
    for card in b_hand:
            if card.startswith("2"):
                b_hand_value += 2
            elif card.startswith("3"):
                b_hand_value += 3
            elif card.startswith("4"):
                b_hand_value += 4
            elif card.startswith("5"):
                b_hand_value += 5
            elif card.startswith("6"):
                b_hand_value += 6
            elif card.startswith("7"):
                b_hand_value += 7
            elif card.startswith("8"):
                b_hand_value += 8
            elif card.startswith("9"):
                b_hand_value += 9
            elif card.startswith("10") or card.startswith("Jack") or card.startswith("Queen") or card.startswith("King"):
                b_hand_value += 10
            elif card.startswith("Ace"):
                if 10 <= b_hand_value <= 21:
                    b_hand_value += 1
                elif b_hand_value < 10:
                    b_hand_value += 11
    return b_hand_value
def get_p_hand_value():
    global p_balance
    global b_balance
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
                    hand_value += 1
                elif hand_value < 10:
                    hand_value += 11
            if hand_value > 21:
                if p_balance <= 0:
                    print("You busted! The bot wins the whole game!")
                    running = False
                else:
                    print("You busted! Your bets go to the bot!")
                    b_balance += bet * 2
                    return hand_value
    return hand_value
def get_silent_p_hand_value():
    global p_balance
    global b_balance
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
                    hand_value += 1
                elif hand_value < 10:
                    hand_value += 11
            if hand_value > 21:
                if p_balance <= 0:
                    running = False
                else:
                    b_balance += bet * 2
                    return hand_value
    return hand_value
p_balance = 100
b_balance = 100
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
        for _ in range(1000):
            for j in range(len(self.cards)):
                switcher = random.randint(0,len(self.cards)-1)
                temp = self.cards[j]
                self.cards[j] = self.cards[switcher]
                self.cards[switcher] = temp
    def __str__(self):
        return "\n".join(self.cards)
p_hand = []
b_hand = []
deck = Deck()
def deal_hand():
    global p_hand, b_hand, deck
    p_hand = []
    b_hand = []
    deck = Deck()
    deck.shuffle()
    for _ in range(2):
        p_hand.append(deck.cards[0])
        deck.cards.pop(0)
        b_hand.append(deck.cards[0])
        deck.cards.pop(0)
running = True
hand_value = 0
b_hand_value = 0
hand_value = get_p_hand_value()
b_hand_value= get_b_hand_value()
while(running):
    deal_hand()
    bet = int(input(f"what would you like to bet this round? Your balance is ${p_balance}\n"))
    while bet > p_balance:
        bet = int(input(f"You only have ${p_balance}. Now, what would you like to bet this round?\n"))
    p_balance -= bet
    b_balance -= bet
    print("Great! You now have $",p_balance,"!")
    print("The hands have been dealt. Your cards are the "+p_hand[0]+" and the "+p_hand[1])
    status = input("Would you like to hit or stand?")
    while(status != "hit" and status != "stand"):
        status = input("Let's try again. Would you like to hit or stand?")
    if status == "hit":
        while(status == "hit"):
            deck.shuffle()
            p_hand.append(deck.cards[0])
            deck.cards.pop(0)
            print("Your hand: ",p_hand)
            hand_value = get_p_hand_value()
            if hand_value > 21:
                b_balance += bet * 2
                status = "stand"
            else:
                status = input("Now, after seeing your new card, Would you like to hit or stand?")
        while b_hand_value < 17 or b_hand_value < hand_value:
            deck.shuffle()
            b_hand.append(deck.cards[0])
            deck.cards.pop(0)
            hand_value = get_silent_p_hand_value()
            b_hand_value = get_b_hand_value()
        if hand_value > b_hand_value:
            print("Your hand's value is ",hand_value,". The bot's hand value is ",b_hand_value,". Therefore, the winner of this hand is the player!")
            p_balance += bet * 2
        elif b_hand_value > hand_value and b_hand_value <= 21:
            print("Your hand's value is ",hand_value,". The bot's hand value is ",b_hand_value,". Therefore, the winner of this hand is the bot!")
            b_balance += bet * 2
        elif b_hand_value > hand_value and hand_value < 22:
            print("Your hand's value is ",hand_value,". The bot's hand value is ",b_hand_value,". Therefore, the winner of this hand is the player, as the bot busted!")
            p_balance += bet * 2
        elif b_hand_value == hand_value:
            print("You and the bot tied at ",hand_value," and the dealer always wins ties, so the bot wins the hand!")
            b_balance += bet * 2
        else:
            b_hand_value = random.randint(17,21)
            print("Your hand's value is ",hand_value,". The bot's hand value is ",b_hand_value,". Therefore, the winner of this hand is the bot!")
            
    elif status == "stand":
        hand_value = get_p_hand_value()
        b_hand_value = get_b_hand_value()
        while b_hand_value < 17:
            deck.shuffle()
            b_hand.append(deck.cards[0])
            deck.cards.pop(0)
            hand_value = get_b_hand_value()
        if hand_value > b_hand_value:
            print("Your hand's value is ",hand_value,". The bot's hand value is ",get_b_hand_value,". Therefore, the winner of this hand is the player!")
            p_balance += bet * 2
        elif b_hand_value > hand_value and b_hand_value <= 21:
            print("Your hand's value is ",hand_value,". The bot's hand value is ",b_hand_value,". Therefore, the winner of this hand is the bot!")
            b_balance += bet * 2
        elif b_hand_value > hand_value:
            print("Your hand's value is ",hand_value,". The bot's hand value is ",b_hand_value,". Therefore, the winner of this hand is the player, as the bot busted!")
            p_balance += bet * 2
        else:
            print("You and the bot tied at ",hand_value," and the dealer always wins ties, so the bot wins the hand!")
            b_balance += bet * 2