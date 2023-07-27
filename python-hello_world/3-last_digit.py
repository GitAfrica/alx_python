#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

def last_digit_message(num):
    if num > 0:
        output = f"{num} is positive."
    elif num < 0:
        output = f"{num} is negative."
    else:
        output = f"{num} is zero."

    return output

print(last_digit_message(number))
