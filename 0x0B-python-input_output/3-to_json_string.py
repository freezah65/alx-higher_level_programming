#!/usr/bin/python3
"""it Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    return json.dumps(my_obj)
