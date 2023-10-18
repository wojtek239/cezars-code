ALPHABET_SIZE = 36


class Decryptor:
    """decrypts given text by cezars-code"""

    @staticmethod
    def decrypt_word_with_key(encrypted_word, shift):
        decrypted_word = ""
        for char in encrypted_word:
            if char.isalpha():
                if char.islower():
                    base = ord("a")
                elif char.isupper():
                    base = ord("A")
                else:
                    continue
                shifted = (ord(char) - base - shift) % ALPHABET_SIZE
                decrypted_word += chr(base + shifted)
            else:
                decrypted_word += char
        return decrypted_word
