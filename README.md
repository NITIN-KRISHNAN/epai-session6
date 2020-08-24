# epai-session6
# First Class Functions Part I
## Topics covered
This session mainly covered Default Values, Docstrings & Annotations, Lambda Expression,
Functional Introspection, Callables, Map, Filter & Zip

[![Poker Rules image](/poker_rules.jpg)]

## Descriptions of functions

Help on module session6:

NAME
    session6

DESCRIPTION
    Modified Poker Best Hand estimator
    This module can be used to find out the winner between two players who are dealt 2 to 5 cards
    based on the rules of poker.
    creates a deck of standard playing cards using for loop and using lambda functions.

FUNCTIONS
    calculate_score(cards)
    
    check_flush(cards)
        Check is all the cards are of the same suit
        :param cards: List of Cards dealt to a player
        :return: True when all the cards are of the same suit
                 False otherwise
    
    check_four_of_a_kind(cards)
        Checks if four cards of the same value are available in the set if cards
        :param cards: List of Cards dealt to a player
        :return: True when four cards of the same value are present in the list of cards
                 False otherwise
    
    check_full_house(cards)
        Checks if there is a single pair and three of a kind available in the list of cards
        :param cards: List of Cards dealt to a player
        :return: True when there is a single pair and three of a kind in the list of cards
                 False otherwise
    
    check_high_card(cards1, cards2)
        Checks which amoungh the two sets of cards has the higher value card
        :param cards1: List of Cards dealt to player 1
        :param cards2: List of Cards dealt to player 2
        :return: 1 if player 1 has higher card
                 2 if player 2 has higher card
                 0 in case of tie
    
    check_one_pair(cards, counts=None)
        Checks if one pair of cards of same value is available in the set if cards
        :param cards: List of Cards dealt to a player
        :return: True when a pair is present in the list of cards
                 False otherwise
    
    check_royal_flush(cards)
        Checks if a there is consecutive sequence of 10, jack, queen, king, ace of the same suit
        :param cards: List of Cards dealt to a player
        :return: True when there is consecutive sequence of 10, jack, queen, king, ace of the same suit
                 False otherwise
        :param cards:
        :return:
    
    check_straight(cards)
            Checks if the cards are in a consecutive order
        :param cards: List of Cards dealt to a player
        :return: True when all the cards are in a consecutive order
                 False otherwise
    
    check_straight_flush(cards)
        Checks if a there is consecutive sequence of cards of the same suit
        :param cards: List of Cards dealt to a player
        :return: True when there is consecutive sequence of cards of the same suit in the list of cards
                 False otherwise
    
    check_three_of_a_kind(cards, counts=None)
        Checks if there cards of the same value are available in the set if cards
        :param cards: List of Cards dealt to a player
        :return: True when four cards of the same value is present in the list of cards
                 False otherwise
    
    check_two_pair(cards)
        Checks if two pairs of cards of the same value are available in the set if cards
        :param cards: List of Cards dealt to a player
        :return: True when two pairs are present in the list of cards
                 False otherwise
    
    create_deck_lambda()
        Creates a deck of cards without using lambda, map
        :return: deck of cards
    
    create_deck_normal()
        Creates a deck of cards without using lambda, map and zip
        :return: deck of cards
    
    find_winner(cards1: 'List of Cards dealt to player 1', cards2: 'List of Cards dealt to player 1')
        Finds the winner of the poker game based on the cards dealt to the two player according to the calculated score
        based on the combinations_check_list.
        :param cards1: List of Cards dealt to player 1
        :param cards2: List of Cards dealt to player 2
        :return: 0 - in case of a tie
                 1 - when player 1 has won
                 2 - when player 2 has won
    
    get_card_val_list(cards)
    
    get_counts(cards)

DATA
    combinations_check_list = [<function check_royal_flush>, <function che...
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen',...
    vals_dict = {'10': 10, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,...

## Test cases
- test_winner
-- Some sample games are tested to check if the function to find overall winner works
- test_doc_string
-- Checks if doc string is available for a few functions
- test_annotations
-- Checks if doc string is available for a find_winner function
- test_deck_normal
- test_deck_lambda
- test_one_pair
- test_two_pair
- test_three_of_kind
- test_straight
- test_flush
- test_full_house
- test_four_of_kind
- test_straight_flush
- test_royal_flush
- test_high_card
- test_cards_input
- test_readme_exists
- test_readme_contents
- test_readme_proper_description
- test_readme_file_for_formatting
- test_indentations
- test_function_name_had_cap_letter
- test_mandatory_fuctions_availability
- test_deck_normal_invalid
- test_deck_lambda_invalid
## Test Results
test_session6.py::test_deck_normal PASSED                                                                                                                                     [  4%]
test_session6.py::test_deck_normal_invalid PASSED                                                                                                                             [  8%]
test_session6.py::test_deck_lambda PASSED                                                                                                                                     [ 12%]
test_session6.py::test_deck_lambda_invalid PASSED                                                                                                                             [ 16%]
test_session6.py::test_one_pair PASSED                                                                                                                                        [ 20%]
test_session6.py::test_two_pair PASSED                                                                                                                                        [ 24%]
test_session6.py::test_three_of_kind PASSED                                                                                                                                   [ 28%]
test_session6.py::test_straight PASSED                                                                                                                                        [ 32%]
test_session6.py::test_flush PASSED                                                                                                                                           [ 36%]
test_session6.py::test_full_house PASSED                                                                                                                                      [ 40%]
test_session6.py::test_four_of_kind PASSED                                                                                                                                    [ 44%]
test_session6.py::test_straight_flush PASSED                                                                                                                                  [ 48%]
test_session6.py::test_royal_flush PASSED                                                                                                                                     [ 52%]
test_session6.py::test_high_card PASSED                                                                                                                                       [ 56%]
test_session6.py::test_cards_input PASSED                                                                                                                                     [ 60%]
test_session6.py::test_winner PASSED                                                                                                                                          [ 64%]
test_session6.py::test_doc_string PASSED                                                                                                                                      [ 68%]
test_session6.py::test_annotations PASSED                                                                                                                                     [ 72%]
test_session6.py::test_readme_exists PASSED                                                                                                                                   [ 76%]
test_session6.py::test_readme_contents PASSED                                                                                                                                 [ 80%]
test_session6.py::test_readme_proper_description PASSED                                                                                                                       [ 84%]
test_session6.py::test_readme_file_for_formatting PASSED                                                                                                                      [ 88%]
test_session6.py::test_indentations PASSED                                                                                                                                    [ 92%]
test_session6.py::test_function_name_had_cap_letter PASSED                                                                                                                    [ 96%]
test_session6.py::test_mandatory_fuctions_availability PASSED                                                                                                                 [100%]

================================================================================ 25 passed in 0.09s =================================================================================

