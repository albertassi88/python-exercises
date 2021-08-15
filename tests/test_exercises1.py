import pytest
from exercises1 import list_numbers


def test_divide_number_with_three_and_five():
    assert list_numbers(15)[-1] == 'FizzBuzz'
    assert list_numbers(3)[-1] == 'Fizz'
    assert list_numbers(5)[-1] == "Buzz"
