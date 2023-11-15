from const import ALPHABET_SIZE


def validate_shift(shift):
    if not isinstance(shift, int) or shift <= 0:
        raise ValueError("Shift must be a positive integer")


def normalize_shift(shift):
    return shift % ALPHABET_SIZE


def shift_character(char, shift_direction, shift):
    validate_shift(shift)

    if char.isalpha() and char.isascii():
        if char.islower():
            base = ord("a")
        elif char.isupper():
            base = ord("A")
        else:
            return char

        normalized_shift = normalize_shift(shift)
        shifted = (ord(char) - base + shift_direction * normalized_shift) % \
                  ALPHABET_SIZE

        return chr(base + shifted)
    return char

# sift ogarnac
# poprawic utils
# ugh

