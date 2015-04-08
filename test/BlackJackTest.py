from unittest import TestCase
from models.deck import Deck
from models.dealer import Dealer

class TestDeck(TestCase):

    def test52Cards(self):
        deck = Deck()
        self.assertEqual(len(deck), 36)

    def testPopACard(self):
        deck = Deck()
        card = deck.pop()

        self.assertEqual(len(deck), 35)
        self.assertEqual(type(card), tuple)
        self.assertEqual(len(card), 2)


class TestDealer(TestCase):

    def testDealCardsInDeck(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.deal()
        self.assertEqual(len(deck), 32)

    def testPlayerCards(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.deal()
        self.assertEqual(len(dealer.player.cards), 2)

    def testDeallerWith2Cards(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.deal()
        self.assertEqual(len(dealer.cards), 2)

    def testDeallerHitPlayer(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.hit_player()
        self.assertEqual(len(dealer.player.cards), 1)

    def testDealerHitForHim(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.hit()
        self.assertEqual(len(dealer.cards), 1)

    def testDealerHitUntil17(self):
        deck = Deck()
        dealer = Dealer(deck)
        dealer.hit_until()
        sum_dealer = sum([d[0] for d in dealer.cards])
        self.assertGreaterEqual(sum_dealer, 17)