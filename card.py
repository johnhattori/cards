#!/usr/bin/env python3

import random

SUITS = ["spades", "clubs", "hearts", "diamonds"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def get_suit_and_rank(self):
        return RANKS[self.rank], SUITS[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(len(SUITS)):
            for rank in range(len(RANKS)):
                self.cards.append(Card(rank, suit))
            
    def render_cards(self):
        for card in self.cards:
            print(card.get_suit_and_rank())

    def shuffle(self):
        random.shuffle(self.cards)    


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.render_cards()

    
