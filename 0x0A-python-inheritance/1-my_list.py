#!/usr/bin/python3

"""an inherited list class MyList."""


class MyList(list):
    """Write a class MyList that inherits from list:"""
    def print_sorted(self):
        print(sorted(self))
