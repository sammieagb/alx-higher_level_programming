#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in revr order alternating upper and lowercase."""
r = 0
for c in range(ord('z'), ord('a') - 1, -1):
print("{}".format(chr(c - r)), end="")
r = 32 if r == 0 else 0
