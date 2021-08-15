def number_phone(letters):
    if not 1 < len(letters) <= 30:
        raise ValueError("Expression with invalid length")
    phone = ''
    for letter in letters.upper():
        if letter in 'ABC':
            phone += '2'
        elif letter in 'DEF':
            phone += '3'
        elif letter in 'GHI':
            phone += '4'
        elif letter in 'JKL':
            phone += '5'
        elif letter in 'MNO':
            phone += '6'
        elif letter in 'PQRS':
            phone += '7'
        elif letter in 'TUV':
            phone += '8'
        elif letter in 'WXYZ':
            phone += '9' 
        elif letter in '-01':
            phone += letter
        else:
            raise ValueError("Invalid character")
    return phone

