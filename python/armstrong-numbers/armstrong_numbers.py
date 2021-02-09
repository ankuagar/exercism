def is_armstrong_number(number):
    return number == sum(map(lambda digit, pow=len(str(number)): int(digit) ** pow, str(number)))
