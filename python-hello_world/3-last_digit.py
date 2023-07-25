#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

import random

number = random.randint(-10000, 10000)

def last_digit_message(num):
    last_digit = num % 10
    output = f"Last digit of {abs(num)} is {abs(last_digit)} and is"

    if num == 0:
        output += " 0"
    elif last_digit == 0:
        output += " 0"
    elif num < 0:
        output += " less than 6 and not 0"
    elif last_digit > 5:
        output += " greater than 5"
    else:
        output += " less than 6 and not 0"

    return output

print(last_digit_message(number))

