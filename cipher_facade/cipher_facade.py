from encrypting.encrypting import Encryptor
# ...
#TODO Menu

class CipherFacade:
    def __init__(self):

        self.history = []
        self.encryptor = Encryptor()

    def encrypt_word_with_key(self, text: str, shift: int):
        encrypted_text = Encryptor.encrypt_word_with_key(text, shift)

        self.history.append({
            "input_text": text,
            "shift": shift,
            "encrypted_text": encrypted_text
        })

        print(f"Given text: {text}")
        print(f"Shift: {shift}")
        print(f"Encrypted text: {encrypted_text}")

        return encrypted_text

# ...
