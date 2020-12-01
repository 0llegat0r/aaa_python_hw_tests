from morse import LETTER_TO_MORSE
import doctest


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode("SOS")
    '... --- ...'
    >>> encode("")
    ''
    >>> encode(" ")
    ' '
    >>> encode("LOW DOT CODED LINE.") \
    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    '.-..      --- .--          -..
     ...
     .-..    ..      -.     .     .-.-.-'
    >>> encode("a")
    Traceback (most recent call last):
    ...
    KeyError: \'a\'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)


if __name__ == "__main__":
    doctest.testmod()
