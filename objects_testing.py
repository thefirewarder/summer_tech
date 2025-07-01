from card import card
from deck import deck
card1 = card(10,"spades")
deck1 = deck()
deck1.shuffle()
for i in range(52):
    print(deck1.deck[i].string())