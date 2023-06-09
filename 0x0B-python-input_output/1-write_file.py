#!/usr/bin/python3
"""A function  that writes a string to a text file (UTF8)
    and returns the number of characters written:"""


def write_file(filename="", text=""):
    """Opens/create a file and writes content in it"""

    with open(filename, 'w',  encoding="utf-8") as f:
        return (f.write(text))
