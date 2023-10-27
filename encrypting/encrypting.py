from const import ALPHABET_SIZE
import json


class Encryptor:
    """encrypt given text by cezars-code"""

    @staticmethod
    def encrypt_word_with_key(word, shift):
        """encrypts word with given shift"""
        encrypted_word = ""
        for char in word:
            if char.isalpha():
                if char.islower():
                    base = ord("a")
                elif char.isupper():
                    base = ord("A")
                else:
                    continue
                shifted = (ord(char) - base + shift) % ALPHABET_SIZE
                encrypted_word += chr(base + shifted)
            else:
                encrypted_word += char
        return encrypted_word
