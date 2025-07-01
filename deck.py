import random
from card import card
class deck:
    def __init__(self):
        self.deck = []
        self.suit_list = ["spades","hearts","clubs","diamonds"]
        for suit_id in self.suit_list:
            for i in range(1,14):
                self.deck.append(card(i,suit_id))
    def shuffle(self):
        
        for i in range(52):
            self.deck[i], self.deck[random.randint(0,51)] = self.deck[random.randint(0,51)], self.deck[i]
