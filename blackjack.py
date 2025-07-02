import random
class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def string(self):
        name = ""
        if self.rank == 13:
            name += "King"
        elif self.rank == 12:
            name += "Queen"
        elif self.rank == 11:
            name += "Jack"
        elif self.rank == 1:
            name += "Ace"
        else:
            name += str(self.rank)
        name += " of "+str(self.suit)
        return name
class deck:
    def __init__(self):
        self.deck = []
        self.suit_list = ["hearts","diamonds","spades","clubs"]
        for i in range(1,14):
            for suit_chosen in self.suit_list:
                self.deck.append(card(suit_chosen,i).string())
    def shuffle(self):
        for i in range(52):
            self.deck[i], self.deck[random.randint(0,51)] = self.deck[random.randint(0,51)] , self.deck[i]
    def __getitem__(self, position):
        return self.deck[position]

    def pop(self, index=0):
        return self.deck.pop(index)
deck1 = deck()
deck1.shuffle()
p_hand = []
b_hand = []
for i in range (2):
    top_card = deck1[0]
    p_hand.append(top_card)
    deck1.pop(0)
for i in range (2):
    top_card = deck1[0]
    b_hand.append(top_card)
    deck1.pop(0)
running = True
balance = 100
bot_balance = 100
have_bet = False
while have_bet == False:
    bet = int(input("How much would you like to bet?"))
    balance -= bet
    bot_bet = random.randint(1,4)*10
    print("Ok! The bot has bet ",bot_bet)
    bot_balance -= bot_bet
    have_bet = True
b_stood = False
print("The hands have been dealt. Your hand has a",p_hand[0],"and a",p_hand[1],". One of the dealer's cards is hidden. The other is",b_hand[0],".")
def play_game():
    while running:
        stood = False
        while stood == False:
            p_action = input("Would you like to hit or stand?").lower
            if p_action == "hit":
                top_card = deck1[0]
                p_hand.append(top_card)
                deck1.pop(0)
                print("Your new card is a"+p_hand[len(p_hand)-1])
                for i in range(len(p_hand)-1):
                    total = 0
                    total += p_hand[i].rank
                    if total >= 21:
                        print("You busted!"):
                            
            elif p_action == "stand":
                print("Ok! It is now the bot's turn.")
                stood = True
            else:
                print("Please choose a valid action from hit or stand.")
        
        while b_stood == False:
            if b_hand[0].rank + b_hand[1].rank >= 17:
                b_stood = True
play_game()
