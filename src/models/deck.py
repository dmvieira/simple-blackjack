import itertools
import random


class Deck(object):
    def __init__(self):
        self.cards = list(itertools.product(range(2, 11), ['Spade', 'Heart', 'Diamond', 'Club']))
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def pop(self):
        return self.cards.pop()