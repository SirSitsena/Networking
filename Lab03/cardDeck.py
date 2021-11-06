import card as c
from random import shuffle as shuffy

class CardDeck:
    deck = []

    def __init__(self):
        for suit in c.Suit:
            for rank in c.Rank:
                self.deck.append( c.Card( suit, rank ))

    def shuffle(self):
       shuffy(self.deck)

    def getCard(self):
        return self.deck.pop()

    def size(self):
        return len(self.deck)

    def reset(self):
        self.deck = []
        self.__init__()
        self.shuffle()