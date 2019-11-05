from deuces import Evaluator, Card
from poker_hands import lower_card, winner, get_hands


def test_get_hands():
    '''Test that we convert a raw line of input cards into 2 hands of Cards'''
    raw_cards = '8C TS KC 9H 4S 7D 2S 5D 3S AC'
    expected_cards = (
        [Card.new('8c'), Card.new('Ts'), Card.new('Kc'), Card.new('9h'), Card.new('4s')],
        [Card.new('7d'), Card.new('2s'), Card.new('5d'), Card.new('3s'), Card.new('Ac')],
    )
    assert get_hands(raw_cards) == expected_cards


def test_lower_card():
    '''Test that we convert a card string to the format deuces wants'''
    assert lower_card('8C') == '8c'


def test_cards_comparison():
    '''
    We are using a third party library for the hand comparisons. Most
    likely they did it right, but lets test just to be sure we are getting what
    we would expect
    '''

    hands = [
        # royal flush beats straight flush
        ('TH JH QH KH AH 9H TH JH QH KH', 1),
        # straight flush beats four-of-a-kind
        ('9H TH JH QH KH 8H 8C 8D 8S 2H', 1),
        # four-of-a-kind beats full house
        ('8H 8C 8D 8S 2H 9H 9C 9D 6D 6H', 1),
        # full house beats flush
        ('9H 9C 9D 6D 6H 2D 7D 4D 5D 6D', 1),
        # flush beats straight
        ('2D 8D 4D 5D 6D 4H 5D 6C 7D 8H', 1),
        # straight beats 3 of a kind
        ('4H 5D 6C 7D 8H 3C 3D 3H KC QH', 1),
        # 3 of a kind beats 2 pairs
        ('3C 3D 3H KC QH 7H 7C 8H 8C KH', 1),
        # 2 pairs beats 1 pair
        ('7H 7C 8H 8C KH KC KD 2H 4D 9C', 1),
        # 1 pair beats high card
        ('2C 2C 4D 6H 8D AC KD JH 3H 5C', 1),
    ]

    # some random scenariors from the problem examples
    random_hands = [
        # 2 full houses, player 1 wins due to higher cards
        ('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D', 1),
        # pair of queens, player 1 wins due to highest card
        ('4D 6S 9H QH QC 3D 6D 7H QD QS', 1),
        # flush with diamonds beats 3 aces
        ('2D 9C AS AH AC 3D 6D 7D TD QD', 2),
        # ace beats queen
        ('5D 8C 9S JS AC 2C 5C 7D 8S QH', 1),
        # paid of 8s beats pair of 5s
        ('5H 5C 6S 7S KD 2C 3S 8S 8D TD', 2),
    ]

    for hand in hands + random_hands:
        assert winner(*get_hands(hand[0])) == hand[1]
