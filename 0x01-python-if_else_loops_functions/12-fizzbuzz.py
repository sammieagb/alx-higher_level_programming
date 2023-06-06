#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
"""Print the numbrs from 1 to 100 separated by a space.

For multiples of three, print Fizz instead of the numbr.
For multiples of five, print Buzz instead of the numbr.
For multiples of three and five, print FizzBuzz instead of the numbr.
"""
for numbr in range(1, 101):
if numbr % 3 == 0 and numbr % 5 == 0:
print("FizzBuzz ", end="")
elif numbr % 3 == 0:
print("Fizz ", end="")
elif numbr % 5 == 0:
print("Buzz ", end="")
else:
print("{} ".format(numbr), end="")
