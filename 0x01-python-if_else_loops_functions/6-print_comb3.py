#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combo of 2 digits in ascending order.

The 2 digits must be different - 01 and 10 are considered identical.
"""
for digt1 in range(0, 10):
for digt2 in range(digt1 + 1, 10):
if digit1 == 8 and digt2 == 9:
print("{}{}".format(digt1, digt2))
else:
print("{}{}".format(digt1, digt2), end=", ")
