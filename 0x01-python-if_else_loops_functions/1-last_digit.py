#!/usr/bin/python3
import random
numbe = random.randint(-10000, 10000)
digit = abs(numbe) % 10
if numbe < 0:
digit = -digit
print("Last digit of {} is {} and is ".format(numbe, digit), end="")
if digit > 5:
print("greater than 5")
elif digit == 0:
print("0")
else:
print("less than 6 and not 0")
