import string 
def is_valid(isbn):
    isbn = isbn.replace('-','')
    if len(isbn) != 10:
        return False

    elif not all(map(lambda x: x in (string.digits + 'X'), isbn)):
        return False

    total = 0    
    for idx, digit in enumerate(isbn):
        if digit == 'X' and idx != 9 :
            return False
        elif digit == 'X':                        
            digit = '10'
        total += int(digit) * (10-idx)
    return total % 11 == 0        
        

