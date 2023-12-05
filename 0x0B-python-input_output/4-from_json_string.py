#!/usr/bin/python3
"""From JSON string to Object"""

import json


def from_json_string(my_str):
    """returns an object (Python data struct) represented by a JSON string"""
    python_obj = json.loads(my_str)
    return python_obj
