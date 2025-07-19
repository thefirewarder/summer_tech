import random
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts","Diamonds","Spades","Clubs"]
        ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for i in range(13):
            rank = ranks[i]
            for j in range(4):
                suit = suits[j]
        self.cards.append(suit," of ",rank)
deck1 = Deck()