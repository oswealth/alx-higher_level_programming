#!/usr/bin/python3
"""A module that defines a Student class"""


class Student:
    """A class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Args:
            attrs (list of str): A list of attributes to retrieve

        Returns:
            dict: A dictionary with the selected attributes
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if type(attr) is str and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json (dict): A dictionary with the new attributes
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
