import math
def classify(number):
    if number <= 0:
        raise ValueError("{} is not a natural nuumber".format(number))
    elif number == 1:
        return 'deficient'
    aliquot_sum = 1
    for i in range(2, math.ceil(math.sqrt(number)), 1):
        if number % i == 0:
            aliquot_sum += i + number / i           
    if aliquot_sum < number:
        return 'deficient'
    elif aliquot_sum == number:
        return 'perfect'
    else:
        return 'abundant'              
        
