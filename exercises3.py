def valid_email_name(email):
    name = email.split('@')[0]
    for letter in name:
        if not letter.isalnum() and not letter in '-_':
            raise ValueError('Invalid email name!')


def valid_website(email):
    website = email.split('@')[1].split('.')[0]
    if not website.isalnum():
            raise ValueError('Invalid website!')


def invalid_extension_length(email):
    extensao = email.split('.')[1]
    if len(extensao) > 3:
            raise ValueError('Invalid_extension_length!')


def valid_email(email):
    if len(email) <= 0:
        raise ValueError('Email empty!')
    elif not email[0].isalpha():
        raise ValueError('Start email with letter!')
    valid_email_name(email)
    valid_website(email)
    invalid_extension_length(email)
    return email

