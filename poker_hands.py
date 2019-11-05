from deuces import Evaluator, Card


evaluator = Evaluator()


def get_hands(line):
    '''
    Get raw line of input cards and return 2 hands of Cards

    Example:

    8C TS KC 9H 4S 7D 2S 5D 3S AC

    Turns into

    (
        (Card('8c'), Card('Ts'), Card('Kc'), Card('9h'), Card('4s')),
        (Card('7d'), Card('2s'), Card('5d'), Card('3s'), Card('Ac')),
    )
    '''
    cards = line.split()
    hand1 = [Card.new(lower_card(card)) for card in cards[:5]]
    hand2 = [Card.new(lower_card(card)) for card in cards[5:]]

    return (hand1, hand2)


def winner(hand1, hand2):
    '''
    Compares 2 hands of Cards (using deuces) and returns the winning hand
    '''
    if evaluator.evaluate([], hand1) < evaluator.evaluate([], hand2):
        return 1
    else:
        return 2


def lower_card(card):
    '''
    Takes capital card face and suit and returns face and lowercase suit
    according to the format deuces likes them.

    Example: 8C -> 8c
    '''
    return card[0] + card[1].lower()


if __name__ == '__main__':
    path = 'hands.txt'

    player1_wins = 0
    player2_wins = 0

    with open(path, 'r') as f:
        for line in f:
            hand1, hand2 = get_hands(line)

            if winner(hand1, hand2) == 1:
                player1_wins += 1
            else:
                player2_wins += 1

            print 'player 1 wins: {}'.format(player1_wins)
            print 'player 2 wins: {}'.format(player2_wins)
