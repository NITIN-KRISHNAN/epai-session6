"""
Modified Poker Best Hand estimator
This module can be used to find out the winner between two players who are dealt 2 to 5 cards
based on the rules of poker.
creates a deck of standard playing cards using for loop and using lambda functions.
"""
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
vals_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}
suits = ['spades', 'clubs', 'hearts', 'diamonds']


def create_deck_normal():
    """
    Creates a deck of cards without using lambda, map and zip
    :return: deck of cards
    """
    deck = []
    for suit in suits:
        for val in vals:
            deck.append((val, suit))
    return deck


def create_deck_lambda():
    """
    Creates a deck of cards without using lambda, map
    :return: deck of cards
    """
    deck = []
    list(map(lambda x: list(map(lambda y: deck.append((x,y)), suits)), vals))
    return deck


def find_winner(cards1:'List of Cards dealt to player 1', cards2:'List of Cards dealt to player 1'):
    """
    Finds the winner of the poker game based on the cards dealt to the two player according to the calculated score
    based on the combinations_check_list.
    :param cards1: List of Cards dealt to player 1
    :param cards2: List of Cards dealt to player 2
    :return: 0 - in case of a tie
            1 - when player 1 has won
            2 - when player 2 has won
    """
    if(len(cards1) != len(cards2)):
        raise ValueError("number of cards should match")
    if(5 <= len(cards2) <= 2):
        raise ValueError("invalid number of cards")
    deck = create_deck_normal()
    if(any(card not in deck  for card in cards1) or any(card not in deck  for card in cards1)):
        raise ValueError("invalid card", cards1, cards2)
    player1_score = calculate_score(cards1)
    player2_score = calculate_score(cards2)
    print(player1_score, player2_score)
    if player1_score > player2_score:
        print('Winner is: Player 1', cards1)
        return 1
    elif player2_score > player1_score:
        print('Winner is: Player 2', cards2)
        return 2
    else:
        res = check_high_card(cards1, cards2)
        return res


def check_royal_flush(cards):
    """
    Checks if a there is consecutive sequence of 10, jack, queen, king, ace of the same suit
    :param cards: List of Cards dealt to a player
    :return: True when there is consecutive sequence of 10, jack, queen, king, ace of the same suit
            False otherwise
    :param cards:
    :return:
    """
    if not check_flush(cards):
        return False
    card_val_list = get_card_val_list(cards)
    return sorted(card_val_list) == [10,11,12,13,14]


def check_straight_flush(cards):
    """
    Checks if a there is consecutive sequence of cards of the same suit
    :param cards: List of Cards dealt to a player
    :return: True when there is consecutive sequence of cards of the same suit in the list of cards
            False otherwise
    """
    return check_flush(cards) and check_straight(cards)


def check_four_of_a_kind(cards):
    """
    Checks if four cards of the same value are available in the set if cards
    :param cards: List of Cards dealt to a player
    :return: True when four cards of the same value are present in the list of cards
            False otherwise
    """
    counts = get_counts(cards)
    return 4 in counts.values()
    pass


def check_full_house(cards):
    """
    Checks if there is a single pair and three of a kind available in the list of cards
    :param cards: List of Cards dealt to a player
    :return: True when there is a single pair and three of a kind in the list of cards
            False otherwise
    """
    counts = get_counts(cards)
    return check_three_of_a_kind(cards, counts) and check_one_pair(cards, counts)


def check_flush(cards):
    """
    Check is all the cards are of the same suit
    :param cards: List of Cards dealt to a player
    :return: True when all the cards are of the same suit
            False otherwise
    """
    return len(set(map(lambda x: x[1], cards))) == 1


def check_straight(cards):
    """Checks if the cards are in a consecutive order
    :param cards: List of Cards dealt to a player
    :return: True when all the cards are in a consecutive order
            False otherwise
    """
    card_val_list = get_card_val_list(cards)
    sorted_card_val_list = sorted(card_val_list)
    if (sorted_card_val_list == list(range(sorted_card_val_list[0],sorted_card_val_list[-1] + 1))
        or (sorted_card_val_list[0] == 2 and sorted_card_val_list[-1] == 14
            and (sorted_card_val_list[1:-1] == [] or
                sorted_card_val_list[1:-1] == list(range(sorted_card_val_list[1], sorted_card_val_list[-2]+1))))):
        return True
    else:
        return False


def check_three_of_a_kind(cards, counts = None):
    """
    Checks if there cards of the same value are available in the set if cards
    :param cards: List of Cards dealt to a player
    :return: True when four cards of the same value is present in the list of cards
            False otherwise
    """
    counts = counts or get_counts(cards)
    return 3 in counts.values()


def check_two_pair(cards):
    """
    Checks if two pairs of cards of the same value are available in the set if cards
    :param cards: List of Cards dealt to a player
    :return: True when two pairs are present in the list of cards
            False otherwise
    """
    counts = get_counts(cards)
    return len(list(filter(lambda x:x==2, counts.values()))) == 2


def check_one_pair(cards, counts = None):
    """
    Checks if one pair of cards of same value is available in the set if cards
    :param cards: List of Cards dealt to a player
    :return: True when a pair is present in the list of cards
            False otherwise
    """
    counts = counts or get_counts(cards)
    return 2 in counts.values()


def check_high_card(cards1, cards2):
    """
    Checks which amoungh the two sets of cards has the higher value card
    :param cards1: List of Cards dealt to player 1
    :param cards2: List of Cards dealt to player 2
    :return: 1 if player 1 has higher card
            2 if player 2 has higher card
            0 in case of tie
    """
    high_card1 = max(map(lambda x : vals_dict[x[0]], cards1))
    high_card2 = max(map(lambda x : vals_dict[x[0]], cards2))
    if high_card1 > high_card2:
        print('Winner is: Player 1', cards1)
        return 1
    elif high_card2 > high_card1:
        print('Winner is: Player 2', cards1)
        return 2
    else:
        print('Its a tie', cards1, cards2)
        return 0


combinations_check_list = [check_royal_flush, check_straight_flush, check_four_of_a_kind, check_full_house, check_flush, check_straight, check_three_of_a_kind, check_two_pair, check_one_pair]


def calculate_score(cards):
    score = 10
    for combination in combinations_check_list:
        if(combination(cards)):
            return score
        score-=1
    return score


def get_counts(cards):
    card_val_list = get_card_val_list(cards)
    counts = {}
    for card_val in set(card_val_list):
        counts.update({card_val: card_val_list.count(card_val)})
    return counts


def get_card_val_list(cards):
    card_val_list = list(map(lambda x : vals_dict[x[0]], cards))
    return card_val_list