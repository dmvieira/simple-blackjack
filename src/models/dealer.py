
class Dealer(object):
    def __init__(self, deck):
        self.deck = deck
        self.cards = list()
        self.player = Player()

    def deal(self):
        self.hit_player()
        self.hit()
        self.hit_player()
        self.hit()

    def hit(self):
        self.cards.append(self.deck.pop())

    def hit_player(self):
        self.player.receive_deal(self.deck.pop())

    def hit_until(self):
        cards_sum = sum([d[0] for d in self.cards])
        while cards_sum < 17:
            self.hit()
            cards_sum = sum([d[0] for d in self.cards])


class Player(object):
    def __init__(self):
        self.cards = list()

    def receive_deal(self, card):
        self.cards.append(card)