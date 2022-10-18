from cardDeck import CardDeck

if __name__ == "__main__":

    deck = CardDeck()
    deck.shuffle()

    while deck.size() > 0:
        card = deck.getCard()
        print("Card {} has value {}".format(card, card.getRank().value))
