import pytest
from exercises5 import valid_email

def test_valid_email():
    assert valid_email('albertassi88@gmail.com') == 'albertassi88@gmail.com'

def test_empty_email():
    with pytest.raises(ValueError, match='Email empty!'):
        valid_email('')

def test_start_email_with_letter():
    with pytest.raises(ValueError, match='Start email with letter!'):
        valid_email('4albertassi88@gmail.com')

def test_valid_email_name():
    name = 'albe*rtassi-88_'
    with pytest.raises(ValueError, match='Invalid email name!'):
        valid_email(f'{name}@gmail.com')

def test_valid_website():
    website = 'gmail+'
    with pytest.raises(ValueError, match='Invalid website!'):
        valid_email(f'albertassi88@{website}.com')

def test_invalid_extension_length():
    extension = 'comm'
    with pytest.raises(ValueError, match='Invalid_extension_length!'):
        valid_email(f'albertassi88@gmail.{extension}')