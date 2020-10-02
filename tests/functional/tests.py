import pytest
from functions.functions import number_is_pair, yes, is_right, solve_simple_function, pythagora_result
import math

def test_num_is_pair():
    no_pair_num = 3485
    pair_num = 3486

    assert not number_is_pair(no_pair_num)

    assert number_is_pair(pair_num)


def test_yes():
    yes_answer = 'y'
    no_answer = 'n'
    non_valid_answer = "djsaid"

    assert yes(yes_answer)
    assert not yes(no_answer)
    with pytest.raises(ValueError):
        yes(non_valid_answer)


def tes_is_right():
    correct = "Nice answer. Are you a programmer???"
    wrong = "EEE wrong answer!"
    right_value, right_answer = True
    wrong_value, wrong_answer = False

    assert is_right(right_value, right_answer) == correct
    assert is_right(wrong_value, wrong_answer) == wrong
    assert is_right(wrong_value, right_answer) == wrong
    assert is_right(right_value, wrong_answer) == wrong


def test_solve_function():
    """
    Imamo funkciju ax + b = c
    gde su a,b i c neke konstante, x je nepoznata
    RESENJE:
        ax +/- b = c
        ax = c -/+ b
        x = (c -/+ b)/a
    :return:
    """
    a = 3
    b = 2
    c = 0
    simple_func_1 = f'{a}x+{b}={c}'
    simple_func_2 = f'{a}x-{b}={c}'
    x1 = solve_simple_function(simple_func_1)
    x2 = solve_simple_function(simple_func_2)

    r1 = ((a*x1) + b)
    r2 = ((a*x2) - b)
    assert r1 == c
    assert r2 == c


def test_third_find_c():
    # setup
    a = 3
    b = 4

    expected_result = math.sqrt(a*a + b*b)
    result = pythagora_result(a, b)
    assert result == expected_result
