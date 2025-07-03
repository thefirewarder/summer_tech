import random
b_stood = False
total = 0
total2 = 0
def check_for_wins():
    if balance <= 0:
        print("You lose! You ran out of coins! Better luck next time...")
        return "over"
    elif bot_balance <= 0:
        print("The bot lost! It ran out of coins! Good job!")
        return "over"
    else:
        return "not_over"
def compare_totals(total,total2):
    if total > total2:
        end_hand("p")
    elif total2 > total:
        end_hand("b")
    else:
        end_hand("t")
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
    def get_rank(self):
        if self.rank >= 10:
            return 10
        elif self.rank == 1:
            return 11
        else:
            return self.rank

class deck:
    def __init__(self):
        self.deck = []
        self.suit_list = ["hearts","diamonds","spades","clubs"]
        for i in range(1,14):
            for suit_chosen in self.suit_list:
                self.deck.append(card(suit_chosen,i))
    def shuffle(self):
        rand = random.randint(0,51)
        for i in range(52):
            self.deck[i], self.deck[rand] = self.deck[rand] , self.deck[i]
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
balance = 100
bot_balance = 100
have_bet = False
def end_hand(winner,bust_status):
    global balance
    global bet
    global bot_balance
    global bot_bet
    global total
    global total2
    if winner == "b":
        bot_balance += bot_bet + bet
        if bust_status != "b":
            print("You had a ",total," and the bot had a ",total2, ". So, the bot wins this hand, for a total of ",bot_bet+bet,". You now have ",balance," and the bot has ",bot_balance)
        for card in p_hand:
            deck1.deck.append(card)
            p_hand.remove(card)
        for card in b_hand:
            deck1.deck.append(card)
            b_hand.remove(card)
    elif winner == "p":
        balance += bot_bet + bet
        if bust_status != "b":
            print("You had a ",total," and the bot had a ",total2, ". So, you win this hand, for a total of ",bot_bet+bet,". You now have ",balance," and the bot has ",bot_balance)
        for card in p_hand:
            deck1.deck.append(card)
            p_hand.remove(card)
        for card in b_hand:
            deck1.deck.append(card)
            b_hand.remove(card)
    else:
        balance += (bot_bet + bet)/2
        bot_balance += (bot_bet + bet)/2
        print("You had a ",total," and the bot had a ",total2, ". So, you tie this hand, each getting a total of ",(bot_bet+bet)/2,". You now have ",balance," and the bot has ",bot_balance)
        for card in p_hand:
            deck1.deck.append(card)
            p_hand.remove(card)
        for card in b_hand:
            deck1.deck.append(card)
            b_hand.remove(card)
def play_game():
    global total
    global total2
    global b_stood
    running = True
    while running:
        stood = False
        while stood == False:
            p_action = input("Would you like to hit or stand?")
            if p_action == "hit":
                top_card = deck1[0]
                p_hand.append(top_card)
                deck1.pop(0)
                print("Your new card is a "+p_hand[len(p_hand)-1].string())
                for i in range(len(p_hand)):
                    total += p_hand[i].get_rank()
                    if total >= 21:
                        for card in p_hand:
                            if card.get_rank() == 11:
                                card.rank = 1
                                break
                            else:
                                print("You busted!")
                                end_hand("b","b")
                                running = False
                            
            elif p_action == "stand":
                print("Ok! It is now the bot's turn.")
                stood = True
            else:
                print(p_action)
                print("Please choose a valid action from hit or stand.")
        
        while b_stood == False:
            for i in range(len(b_hand)-1):
                total2 += b_hand[i].get_rank()
            if 17 <= total2 <= 21:
                compare_totals(total, total2)
                b_stood = True
            if total2 > 21:
                print("The bot busted!")
                end_hand("p","b")
                running=False
while have_bet == False:
    bet = int(input("How much would you like to bet?"))
    balance -= bet
    bot_bet = random.randint(1,4)*10
    print("Ok! The bot has bet ",bot_bet)
    bot_balance -= bot_bet
    have_bet = True
print("The hands have been dealt. Your hand has a",p_hand[0].string(),"and a",p_hand[1].string(),". One of the bot's cards is hidden. The other is",b_hand[0].string(),".")
if check_for_wins() == "not_over":
    play_game()