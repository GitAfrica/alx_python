#!/usr/bin/python3
def last_digit_message(num):
    last_digit = num % 10
    output = f"Last digit of {num} is {last_digit} and is"

    if last_digit > 5:
        output += " greater than 5"
    elif last_digit == 0:
        output += " 0"
    else:
        output += " less than 6 and not 0"

    return output


print(last_digit_message(4205))
print(last_digit_message(-626))
print(last_digit_message(1144))
print(last_digit_message(-9200))
print(last_digit_message(5247))
print(last_digit_message(-9318))
print(last_digit_message(3369))
print(last_digit_message(-5224))
print(last_digit_message(-4485))
print(last_digit_message(3850))
print(last_digit_message(5169))
