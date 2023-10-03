#!/usr/bin/python3
"""a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything except 'first_name'.
    """

    __slots__ = ["first_name"]
