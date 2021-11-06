from enum import Enum

class Card:
    def __init__(self, suit, rank):
        assert isinstance(suit, Suit)
        assert isinstance(rank, Rank)
        self._suit = suit
        self._rank = rank

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self._suit

    def __str__(self):
        return self._rank.name + " of " + self._suit.name 

#----------------------------------------

class Suit(Enum):
    Spades = 1
    Hearts = 2
    Diamonds = 3
    Clubs = 4

class Rank(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

