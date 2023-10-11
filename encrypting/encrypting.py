class Encryptor:
    def __init__(self, shift):
        self.shift = shift

    def encrypt_word_with_key(self, word, key):
        encrypted_word = ""
        for char in word:
            if char.isalpha():
                shifted = ord(char) + (key % 26)
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    encrypted_word += chr(shifted)
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    encrypted_word += chr(shifted)
            else:
                encrypted_word += char
        return encrypted_word
