#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(numbr):
"""Prints the last digit of a numbr and return it."""
print(abs(numbr) % 10, end="")
return (abs(numbr) % 10)
