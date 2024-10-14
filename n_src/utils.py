
import sqlalchemy.types as types
import logging

# Set up logging configuration
logging.basicConfig(level=logging.ERROR)

def write_file(filename: str, list_of_strings: list[str]) -> None:
    """
    Writes a list of strings to a file, with each string on a new line.

    :param filename: The name of the file to write to.
    :param list_of_strings: A list of strings to be written to the file.
    """
    try:
        with open(filename, "w") as f:
            s = "\n".join(list_of_strings)
            f.write(s)
    except IOError as e:
        logging.error(f"An error occurred while writing to the file: {e}")


class LowerCaseString(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if not isinstance(value, str):
            raise TypeError("Expected a string value")
        return value.lower()


class UpperCaseString(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if not isinstance(value, str):
            raise TypeError("Expected a string value")
        return value.upper()


class TitleCaseString(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if not isinstance(value, str):
            raise TypeError("Expected a string value")
        return value.title()


def capitalize_words(words: list[str]) -> str:
    """
    Capitalizes each word in a list and joins them into a single string.

    :param words: A list of words to be capitalized.
    :return: A string with each word capitalized and joined.
    """
    return ''.join(word.capitalize() for word in words)


def snake_to_pascal(string: str) -> str:
    """
    Converts a snake_case string to PascalCase.

    :param string: The snake_case string to be converted.
    :return: The converted PascalCase string.

    Example:
    >>> snake_to_pascal('example_string')
    'ExampleString'

    Edge Case:
    >>> snake_to_pascal('')
    ''
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    if not string:
        return ''
    return capitalize_words(string.split('_'))


def snake_to_words_or_label(string: str, separator=" ") -> str:
    """
    Converts a snake_case string to a space-separated or other separator format.

    :param string: The snake_case string to be converted.
    :param separator: The separator to use between words (default is space).
    :return: The converted string with words separated by the chosen separator.

    Example:
    >>> snake_to_words_or_label('example_string', separator=' ')
    'Example String'
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    if not string:
        return ''
    return separator.join(word.capitalize() for word in string.split('_'))


def snake_to_words(string: str) -> str:
    """
    Converts a snake_case string to space-separated words.

    :param string: The snake_case string to be converted.
    :return: The converted string with space-separated words.
    """
    return snake_to_words_or_label(string, separator=" ")


def snake_to_label(string: str) -> str:
    """
    Converts a snake_case string to a label format (space-separated words with capitalized first letters).

    :param string: The snake_case string to be converted.
    :return: The converted label string.
    """
    return snake_to_words_or_label(string, separator=" ")


def snake_to_camel(string: str) -> str:
    """
    Converts a snake_case string to camelCase.

    :param string: The snake_case string to be converted.
    :return: The converted camelCase string.

    Example:
    >>> snake_to_camel('example_string')
    'exampleString'
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    if not string:
        return ''
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])


def camel_to_pascal(string: str) -> str:
    """
    Converts a camelCase string to PascalCase.

    :param string: The camelCase string to be converted.
    :return: The converted PascalCase string.

    Example:
    >>> camel_to_pascal('exampleString')
    'ExampleString'
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    if not string:
        return ''
    return string[0].upper() + string[1:]


def camel_to_snake(name: str) -> str:
    """
    Converts a camelCase or PascalCase string to snake_case.

    :param name: The camelCase or PascalCase string to be converted.
    :return: The converted snake_case string.

    Example:
    >>> camel_to_snake('ExampleString')
    'example_string'
    """
    if not isinstance(name, str):
        raise ValueError("Input must be a string.")
    if not name:
        return ''
    snake_case_name = ''
    for i, char in enumerate(name):
        if char.isupper() and i != 0:
            snake_case_name += '_'
        snake_case_name += char.lower()
    return snake_case_name


def pascal_to_camel(string):
    # convert the first letter of the string to lowercase
    camel = string[0].lower() + string[1:]

    # replace each instance of an uppercase letter with an underscore followed by the lowercase version of the same letter
    return camel.replace('_', '')


def pascal_to_snake(string):
    # insert an underscore before each uppercase letter and convert the entire string to lowercase
    return ''.join(['_' + letter.lower() if letter.isupper() else letter for letter in string]).lstrip('_')


def pascal_to_words(string):
    # Insert a space before each uppercase letter
    words = ''.join([' ' + letter if letter.isupper() else letter for letter in string]).strip()

    # Capitalize the first letter of each word
    return ' '.join(word.capitalize() for word in words.split())

