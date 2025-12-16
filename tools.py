import random
import re

class tokens:
    def __init__(self):
        #self.general = [r'\n', r'\r', r'\t', r'\0']
        #self.anchors = [r'\G', r'^', r'$', r'\A', r'\Z', r'\z', r'\b', r'\B']
        #self.meta_sequences =[]
        #self.flag_modifiers = ['g','m','i','x','s','u','X','U','A','J','n','xx']
        '''self.common_tokens = [
            r'[~]', r'[^~]', r'[a-z]', r'[^a-z]', r'[a-zA-Z]',
            r'.', r'~|~', r'\s', r'\S', r'\d', r'\D',
            r'\w', r'\W', r'(?:~)', r'(~)',
            r'a?', r'a*', r'a+', r'a{%}',
            r'^', r'$', r'\b', r'\B']'''
        self.regex_commands = [
            "~",
            "%",
            ".",
            "^",
            "$",
            "\\",
            "[~]",
            "[^~]",
            "[a-z]",
            "[A-Z]",
            "[0-9]",
            r"\d",
            r"\D",
            r"\w",
            r"\W",
            r"\s",
            r"\S",
            "*",
            "+",
            "?",
            "{%}",
            "{%,}",
            "{%,%}",
            "(~)",
            "(?:~)",
            "(?<~>~)",
            r"(?=~)",
            r"(?!~)",
            r"(?<=~)",
            r"(?<!~)",
            "^",
            "$",
            r"\b",
            r"\B",
            "i",
            "m",
            "s",
            "x",
            r"^\d{3}-\d{2}-\d{4}$",
            "(~|~)"
        ]

    def get_random_value(self):
        # Get all attributes of the class that are lists
        lists = [getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), list)]

        # Flatten the lists into a single list
        all_values = [item for list in lists for item in list]

        # Randomly select one value from the flattened list
        if all_values:  # Check if the list is not empty
            return random.choice(all_values)

        return None  # Return None if there are no values


def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False