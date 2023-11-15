from utils import shift_character, validate_shift


class Encryptor:
    """encrypt given text by cezars-code"""

    @staticmethod
    def encrypt_word_with_key(word, shift):
        """encrypts word with given shift"""
        encrypted_word = ""
        for char in word:
            encrypted_word += shift_character(char, 1, shift)

        return encrypted_word

