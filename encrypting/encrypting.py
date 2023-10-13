class Encryptor:
    """encrypt given text by cezars-code"""
    alphabet_size = 36

    def __init__(self, shift):
        self.shift = shift

    def encrypt_word_with_key(self, word, key):
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
                shifted = (ord(char) - base + key) % self.alphabet_size
                encrypted_word += chr(base + shifted)
            else:
                encrypted_word += char
        return encrypted_word
