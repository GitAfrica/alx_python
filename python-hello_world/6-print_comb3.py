#!/usr/bin/python3
result = ""
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        result += "{:02d}".format(tens_digit * 10 + ones_digit) + ", "

print(result[:-2])  


        

