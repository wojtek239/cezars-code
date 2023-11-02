from const import ALPHABET_SIZE


def shift_character(char, shift_direction, shift):
    if char.isalpha():
        if char.islower():
            base = ord("a")
        elif char.isupper():
            base = ord("A")
        else:
            return char
        shifted = (ord(char) - base + shift_direction * shift) % ALPHABET_SIZE
        return chr(base + shifted)
    return char
