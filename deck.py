from card import card
class deck:
    def __init__(self):
        self.deck = []
        self.rank_list = ["spades","hearts","clubs","diamonds"]
        for suit_id in self.rank_list:
            for i in range(1,14):
                self.deck.append(card(i,suit_id))