from utils import shift_character


class Decryptor:
    """decrypts given text by cezars-code"""

    @staticmethod
    def decrypt_word_with_key(word, shift):
        """decrypts word with given key"""
        decrypted_word = ""
        for char in word:
            decrypted_word += shift_character(char, -1, shift)
        return decrypted_word
