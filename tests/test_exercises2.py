import pytest
from exercises2 import number_phone


def test_letters_turn_phone_numbers():
    assert number_phone('ABC') == '222'
    assert number_phone('DEF') == '333'
    assert number_phone('GHI') == '444'
    assert number_phone('JKL') == '555'
    assert number_phone('MNO') == '666'
    assert number_phone('PQRS') == '7777'
    assert number_phone('TUV') == '888'
    assert number_phone('WXYZ') == '9999'
    assert number_phone('-01') == '-01'


def test_expression_empty():
    with pytest.raises(ValueError):
        number_phone("")


def test_expression_long():
    letters_long = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    with pytest.raises(ValueError):
        number_phone(letters_long)  


def test_expression_with_invalid_chars():
    with pytest.raises(ValueError):
        number_phone(('%$'))