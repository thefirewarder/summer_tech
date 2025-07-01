class card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
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
        name += " of "+self.suit
        return name