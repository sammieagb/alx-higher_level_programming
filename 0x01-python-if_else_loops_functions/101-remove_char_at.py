#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(str, p):
"""Create a copy of the string without the char at position p."""
if p < 0:
return (str)
return (str[:p] + str[p+1:])
