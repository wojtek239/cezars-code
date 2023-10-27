from encrypting.encrypting import Encryptor
from decrypting.decrytping import Decryptor
import json


class CipherFacade:
    def __init__(self):
        self.history = []
        self.__is_running = True
        self.CHOICES = {
            '1': self.encrypt_text,
            '2': self.decrypt_text,
            '3': self.show_history,
            '4': self.encrypt_text_from_file_and_save,
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
        print("Wrong. Please choose only from 1 to 7.")

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

    def decrypt_text(self):
        text = input("Please enter text to decrypt: ")
        shift = int(input("please enter shift: "))

        decrypted_text = Decryptor.decrypt_word_with_key(text, shift)
        self.history.append({
            "input_text": text,
            "shift": shift,
            "decrypted text": decrypted_text
        })
        print(f"Given text: {text}")
        print(f"Shift: {shift}")
        print(f"Decrypted text: {decrypted_text}")
        return decrypted_text

    def show_history(self):
        if not self.history:
            print("History is empty.")
        else:
            print("History:")
            for item in self.history:
                print(f"Input text: {item['input_text']}")
                print(f"Shift: {item['shift']}")
                if 'encrypted_text' in item:
                    print(f"Encrypted text: {item['encrypted_text']}")
                if 'decrypted_text' in item:
                    print(f"Decrypted text: {item['decrypted_text']}")
                print("-" * 30)

    def encrypt_text_from_file_and_save(self):
        filename = input("Enter the filename to encrypt and save: ")
        try:
            with open(filename, 'r') as file:
                text = file.read()
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
            self.ask_to_save_to_history()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_to_file(self):
        filename = input("Enter the filename to save history (e.g., history.json): ")
        with open(filename, 'w') as file:
            json.dump(self.history, file)
        print(f"History saved to {filename}")

    def exit(self):
        self.__is_running = False
        print("See You next time!")
