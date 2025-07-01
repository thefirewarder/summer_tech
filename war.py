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
hand2 = deck1.string()
running = True
while running:
    to_be_played = hand1[0]
    hand1.pop(0)
    hand1.append(to_be_played)





