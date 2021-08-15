import pytest
from exercises4 import filter_valid_emails

list_email = [
    'albertassi88@gmail.com',
    'luiza#bol.com',
    'damasceno@yahoo.com',
    'silva@gmail.comk'
]

def test_filter_valid_emails():
    assert filter_valid_emails(list_email) == ['albertassi88@gmail.com', 'damasceno@yahoo.com']