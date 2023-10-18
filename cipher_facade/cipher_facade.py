from encrypting.encrypting import Encryptor
from decrypting.decrytping import Decryptor


class CipherFacade:
    def __init__(self):
        self.history = []
        self.__is_running = True
        self.CHOICES = {
            '1': self.encrypt_text,
            '7': self.exit,
        }
        self.initialize()

    def initialize(self):
        while self.__is_running:
            self.show_menu()
            self.get_and_execute_choice()

    def show_menu(self):
        menu = (
            '''
            Menu:
            1. Encrypt text
            2. Decrypt text
            3. Show history
            4. Encrypt from file and save
            5. Save to file
            6. Import results from file to memory
            7. Exit 
            file sa typu JSON
            '''
        )
        print(menu)

    def get_and_execute_choice(self):
        user_choice = input("Choose an option: ")
        self.CHOICES.get(user_choice, self.show_error)()

    def show_error(self):
        print("Wrong. Please choose only from 1, 2, 3, or 4.")

    def encrypt_text(self):
        text = input("Please enter text to encrypt: ")
        shift = int(input("Please enter shift: "))

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

    def exit(self):
        self.__is_running = False
        #TODO
        # zapytac uzytkownika czy nie chce zapisac histori do pliku
        print("See You next time!")

    # def run_menu(self):
    #
    #     while True:
    #         choice = input("Choose an option: ")
    #
    #         if choice == "1":
    #             text = input("Please enter text to encrypt: ")
    #             shift = int(input("Please enter shift: "))
    #             cipher_facade.encrypt_word_with_key(text, shift)
    #         elif choice == "2":
    #             text = input("Please enter text to decrypt: ")
    #             shift = int(input("Please enter shift: "))
    #             cipher_facade.decrypt_word_with_key(text, shift)
    #         elif choice == "3":
    #             print("History:")
    #             for entry in cipher_facade.history:
    #                 print(f"Entered text: {entry['input_text']}")
    #                 print(f"Shift: {entry['shift']}")
    #                 if 'encrypted_text' in entry:
    #                     print(f"Encrypted text: {entry['encrypted_text']}")
    #                 elif 'decrypted_text' in entry:
    #                     print(f"Decrypted text: {entry['decrypted_text']}")
    #                 print("\n")
    #         elif choice == "4":
    #             print("See You next time!")
    #             break
    #         else:
    #             print("Wrong. Please choose only from 1, 2, 3, or 4.")

    # def decrypt_word_with_key(self, text: str, shift: int):
    #     decrypted_text = self.decryptor.decrypt_word_with_key(text, shift)
    #     self.history.append({
    #         "input_text": text,
    #         "shift": shift,
    #         "decrypted_text": decrypted_text
    #     })
    #     print(f"Given text: {text}")
    #     print(f"Shift: {shift}")
    #     print(f"Decrypted text: {decrypted_text}")
    #     return decrypted_text
