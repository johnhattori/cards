#!/usr/bin/env python3

class Card:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s


if __name__ == "__main__":
    deck = []
    for suit in range(4):
        for rank in range(13):
            deck.append(Card(rank, suit))
    print(deck[0].rank, deck[-1].suit)    
