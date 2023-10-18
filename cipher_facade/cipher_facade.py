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


def run_menu(cipher_facade):
    menu = '''
    Menu:
    1. Encrypting text
    2. History
    3. Exit
    '''

    while True:
        print(menu)
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Pls enter text to encrypt: ")
            shift = int(input("Pls enter shift: "))
            facade.encrypt_word_with_key(text, shift)
        elif choice == "2":
            print("History:")
            for entry in facade.history:
                print(f"Entered text: {entry['input_text']}")
                print(f"Shift: {entry['shift']}")
                print(f"Encrypted text: {entry['encrypted_text']}")
                print("\n")
        elif choice == "3":
            print("See You next time!")
            break
        else:
            print("Wrong. Pls choose only from 1, 2 or 3.")


if __name__ == "__main__":
    facade = CipherFacade()
    run_menu(facade)


