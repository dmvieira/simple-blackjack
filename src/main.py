from models.dealer import Dealer
from models.deck import Deck


def start():
    deck = Deck()
    dealer = Dealer(deck)
    dealer.deal()
    dealer_cards = dealer.cards
    player_cards = dealer.player.cards

    print "Dealer: %s" % str(dealer_cards[0])
    print "Player: %s" % str(player_cards)

    player_sum = sum([p[0] for p in player_cards])

    while player_sum < 21:
        choice = raw_input("H)it or S)tay:")
        if choice.upper() == 'H':
            dealer.hit_player()
            player_sum = sum([p[0] for p in player_cards])
        elif choice.upper() == 'S':
            break
        print "Player: %s" % str(player_cards)

    dealer.hit_until()

    dealer_sum = sum([d[0] for d in dealer_cards])

    print "Dealer: %s" % str(dealer_cards)
    print "Player: %s" % str(player_cards)

    if player_sum > 21 or dealer_sum > player_sum:
        print "You Lose! :("

    elif player_sum == dealer_sum:
        print "You Tie..."

    else:
        print "You Win! :)"

if __name__ == '__main__':
    start()