def list_numbers(number):
    list_number = []
    for num in range(1, number + 1):
        if num % 15 == 0:
            list_number.append("FizzBuzz")
        elif num % 3 == 0:
            list_number.append("Fizz")
        elif num % 5 == 0:
            list_number.append("Buzz")
        else:
            list_number.append(num)
    return list_number

