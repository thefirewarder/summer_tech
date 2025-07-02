from card import card
from deck import deck
deck1 = deck()
deck1.shuffle()
hand1 = []
hand2 = []
for i in range(26):
    deal = deck1.deck[len(deck1.deck)-1]
    deck1.deck.pop()
    hand1.append(deal)
hand2 = deck1
running = True
while running:
    to_be_played = hand1[0]
    hand1.pop(0)
    to_be_played2 = hand2[0]
    hand2.pop(0)
    if to_be_played > to_be_played2:
        hand1.append(to_be_played)
        hand1.append(to_be_played2)
    elif to_be_played < to_be_played2:
        hand2.append(to_be_played)
        hand2.append(to_be_played2)
    if len(hand1) == 52:
        print("Player 1 wins!")
        running = False
    elif len(hand2) == 52:
        print("Player 2 wins!")
        running = False
    else:
        print("Player 1 played a "+to_be_played+" and Player 2 played a "+to_be_played2+". ")
    





