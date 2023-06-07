#!/usr/bin/python3
import random
numbr = random.randint(-10000, 10000)
if numbr >= 0:
    last_digit = numbr % 10
else:
    last_digit = ((-numbr % 10) * -1)

message = f"Last digit of {numbr} is {last_digit}"

if last_digit == 0:
    print(f"{message} and is 0")
elif last_digit > 5 and last_digit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
