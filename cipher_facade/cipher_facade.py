from encrypting.encrypting import Encryptor
# ...


class CipherFacade:
    def __init__(self, shift):
        self.shift = shift
        self.encryptor = Encryptor(self.shift)

    def encrypt_word_with_key(self, text):
        return self.encryptor.encrypt_word_with_key(text)

# ...
