from encrypting.encrypting import Encryptor
# ...
#TODO Menu

class CipherFacade:
    def __init__(self):
        pass

    def encrypt_word_with_key(self, text: str, shift: int):
        # input text, shift
        encrypted_text = Encryptor.encrypt_word_with_key(text, shift)
        # zapis do histori
        # wyswietlenie informacji dla uzytkownika
        return encrypted_text

# ...
