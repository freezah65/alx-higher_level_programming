#!/usr/bin/python3
"""it defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
