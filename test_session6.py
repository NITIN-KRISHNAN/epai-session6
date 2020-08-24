import session6
import pytest
import os
import re
import inspect
import session6

MANDATORY_FUNCTIONS = [
    'create_deck_normal',
    'create_deck_lambda',
    'find_winner'
    ]

DECK = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]

def test_deck_normal():
    deck = session6.create_deck_normal()
    assert deck.sort() == DECK.sort(), "Not a Standard deck"


def test_deck_normal_invalid():
    deck = session6.create_deck_normal()
    res = ('55', 'hammer') in deck
    assert res == False, "Not a Standard deck"


def test_deck_lambda():
    deck = session6.create_deck_lambda()
    assert deck.sort() == DECK.sort(), "Not a Standard deck"


def test_deck_lambda_invalid():
    deck = session6.create_deck_lambda()
    res = ('55', 'hammer') in deck
    assert res == False, "Not a Standard deck"


def test_one_pair():
    res = session6.check_one_pair([('2', 'spades'), ('2', 'diamonds')])
    assert res == True, "Fail test_one_pair"
    res = session6.check_one_pair([('2', 'spades'), ('2', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == True, "Fail test_one_pair"
    res = session6.check_one_pair([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_one_pair"


def test_two_pair():
    res = session6.check_two_pair([('2', 'spades'), ('2', 'diamonds')])
    assert res == False, "Fail test_two_pair"
    res = session6.check_two_pair([('2', 'spades'), ('2', 'diamonds'), ('4', 'diamonds'), ('4', 'spades'), ('6', 'diamonds')])
    assert res == True, "Fail test_two_pair"
    res = session6.check_two_pair([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_two_pair"


def test_three_of_kind():
    res = session6.check_three_of_a_kind([('2', 'spades'), ('2', 'diamonds'), ('2', 'hearts')])
    assert res == True, "Fail test_three_of_kind"
    res = session6.check_three_of_a_kind([('2', 'spades'), ('2', 'diamonds'), ('2', 'hearts'), ('4', 'spades'), ('6', 'diamonds')])
    assert res == True, "Fail test_three_of_kind"
    res = session6.check_three_of_a_kind([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_three_of_kind"


def test_straight():
    res = session6.check_straight([('2', 'spades'), ('3', 'spades'), ('4', 'spades')])
    assert res == True, "Fail test_straight"
    res = session6.check_straight([('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'hearts'), ('ace', 'spades')])
    assert res == True, "Fail test_straight"
    res = session6.check_straight([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_straight"


def test_flush():
    res = session6.check_flush([('2', 'spades'), ('3', 'spades'), ('4', 'spades')])
    assert res == True, "Fail test_flush"
    res = session6.check_flush([('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('9', 'spades'), ('king', 'spades')])
    assert res == True, "Fail test_flush"
    res = session6.check_flush([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_flush"



def test_full_house():
    res = session6.check_full_house([('2', 'spades'), ('3', 'spades'), ('4', 'spades')])
    assert res == False, "Fail test_full_house"
    res = session6.check_full_house([('2', 'spades'), ('2', 'diamonds'), ('4', 'diamonds'), ('4', 'spades'), ('4', 'clubs')])
    assert res == True, "Fail test_full_house"
    res = session6.check_full_house([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_full_house"


def test_four_of_kind():
    res = session6.check_four_of_a_kind([('2', 'spades'), ('2', 'diamonds'), ('2', 'hearts'), ('2', 'clubs')])
    assert res == True, "Fail test_four_of_kind"
    res = session6.check_four_of_a_kind([('2', 'spades'), ('2', 'diamonds'), ('2', 'hearts'), ('2', 'clubs'), ('6', 'diamonds')])
    assert res == True, "Fail test_four_of_kind"
    res = session6.check_four_of_a_kind([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_four_of_kind"


def test_straight_flush():
    res = session6.check_straight_flush([('2', 'spades'), ('3', 'spades'), ('4', 'spades')])
    assert res == True, "Fail test_straight_flush"
    res = session6.check_straight_flush([('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('ace', 'spades')])
    assert res == True, "Fail test_straight_flush"
    res = session6.check_straight_flush([('2', 'spades'), ('king', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds')])
    assert res == False, "Fail test_straight_flush"


def test_royal_flush():
    res = session6.check_royal_flush([('2', 'spades'), ('3', 'spades'), ('4', 'spades')])
    assert res == False, "Fail test_straight"
    res = session6.check_royal_flush([('2', 'spades'), ('3', 'spades'), ('4', 'hearts'), ('5', 'spades'), ('ace', 'spades')])
    assert res == False, "Fail test_straight"
    res = session6.check_royal_flush([('10', 'spades'), ('jack', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('ace', 'spades')])
    assert res == True, "Fail test_straight"


def test_high_card():
    res = session6.check_high_card([('2', 'spades'), ('3', 'spades'), ('4', 'spades')], [('2', 'hearts'), ('ace', 'spades'), ('4', 'diamonds')])
    assert res == 2, "Fail test_high_card"
    res = session6.check_high_card([('2', 'spades'), ('3', 'spades'), ('jack', 'spades')], [('2', 'clubs'), ('5', 'clubs'), ('4', 'diamonds')])
    assert res == 1, "Fail test_high_card"
    res = session6.check_high_card([('10', 'spades'), ('jack', 'spades'), ('king', 'diamonds'), ('queen', 'spades'), ('8', 'spades')],
                                   [('10', 'diamonds'), ('ace', 'spades'), ('queen', 'diamonds'), ('3', 'spades'), ('5', 'spades')])
    assert res == 2, "Fail test_high_card"
    res = session6.check_high_card([('10', 'spades'), ('jack', 'spades'), ('king', 'spades'), ('queen', 'spades'), ('ace', 'spades')],
                                   [('10', 'diamonds'), ('jack', 'diamonds'), ('king', 'diamonds'), ('queen', 'diamonds'), ('ace', 'diamonds')])
    assert res == 0, "Fail test_high_card"


def test_cards_input():
    res = session6.find_winner([('2', 'spades'), ('3', 'spades'), ('4', 'spades')], [('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds')])
    with pytest.raises(ValueError):
        res = session6.find_winner([('2', 'spades'), ('3', 'spades'), ('4', 'spades')], [('3', 'diamonds'), ('4', 'diamonds')])
    with pytest.raises(ValueError):
        res = session6.find_winner([('2', 'spades'), ('3', 'spades'), ('4', 'spades')], [('4', 'diamonds')])
    with pytest.raises(ValueError):
        res = session6.find_winner([('34', 'spades'), ('3', 'spades'), ('4', 'fidget spinner')], [('4', 'diamonds')])


def test_winner():
    #game 1
    res = session6.find_winner([('2', 'spades'), ('3', 'spades'), ('4', 'spades')], [('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds')])
    assert res == 0, "Fail test_winner"

    #game 2
    res = session6.find_winner([('ace', 'spades'), ('3', 'spades'), ('4', 'spades')], [('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds')])
    assert res == 2, "Fail test_winner"

    #game 3
    res = session6.find_winner([('2', 'spades'), ('2', 'diamonds'), ('2', 'clubs')], [('7', 'clubs'), ('3', 'diamonds'), ('4', 'diamonds')])
    assert res == 1, "Fail test_winner"

    #game 4
    res = session6.find_winner([('2', 'spades'), ('3', 'diamonds'), ('9', 'spades')], [('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds')])
    assert res == 2, "Fail test_winner"

    #game 5
    res = session6.find_winner([('2', 'spades'), ('3', 'spades'), ('4', 'spades'),  ('ace', 'spades'), ('5', 'spades')], [('ace', 'diamonds'), ('5', 'hearts'),('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds')])
    assert res == 1, "Fail test_winner"

def test_doc_string():
    assert session6.create_deck_normal.__doc__ != None, "DocString missing in create_deck_normal"
    assert session6.find_winner.__doc__ != None, "DocString missing in find_winner"


def test_annotations():
    assert session6.find_winner.__annotations__ != {}, "annotations missing in find_winner"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_mandatory_fuctions_availability():
    MANDATORY_FUNCTIONS_AVAILABILITY = True
    f = open("session6.py", "r")
    content = f.read()
    f.close()
    for c in MANDATORY_FUNCTIONS:
        if c not in content:
            MANDATORY_FUNCTIONS_AVAILABILITY = False
            pass
    assert MANDATORY_FUNCTIONS_AVAILABILITY == True, "You have not implemented all the functions"