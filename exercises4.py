from exercises3 import valid_email

list_email = [
    'albertassi88@gmail.com',
    'luiza#bol.com',
    'damasceno@yahoo.com',
    'silva@gmail.comk'
]

def filter_valid_emails(emails):
    list_valid = []
    for email in emails:
        try:
            valid_email(email)
        except ValueError as error:
            print(error)
        else:
            list_valid.append(email) 
    return list_valid

