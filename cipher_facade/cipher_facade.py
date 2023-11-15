from encrypting.encrypting import Encryptor
from decrypting.decrypting import Decryptor
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
            '5': self.save_to_file,
            '6': self.import_history_from_file,
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
            5. Save history to file
            6. Import history from file
            7. Exit
            '''
        )
        print(menu)

    def get_and_execute_choice(self):
        user_choice = input("Choose an option: ")
        self.CHOICES.get(user_choice, self.show_error)()

    def show_error(self):
        print("Wrong. Please choose only from 1 to 7.")

    def encrypt_text(self):
        try:
            text = input("Please enter text to encrypt: ")
            shift = int(input("Please enter shift: "))

            if shift < 0:
                raise ValueError("Shift must be positive integer")

            encrypted_text = Encryptor.encrypt_word_with_key(text, shift)
            self.history.append({
                "input_text": text,
                "shift": shift,
                "encrypted_text": encrypted_text
            })
            print(f"Given text: {text}")
            print(f"Shift: {shift}")
            print(f"Encrypted text: {encrypted_text}")

        except ValueError as e:
            print(f"Error: {e}")

    def decrypt_text(self):
        try:
            text = input("Please enter text to decrypt: ")
            shift = int(input("Please enter shift: "))

            if shift < 0:
                raise ValueError("Shift must be a positive integer")

            decrypted_text = Decryptor.decrypt_word_with_key(text, shift)
            self.history.append({
                "input_text": text,
                "shift": shift,
                "decrypted_text": decrypted_text
            })
            print(f"Given text: {text}")
            print(f"Shift: {shift}")
            print(f"Decrypted text: {decrypted_text}")
        except ValueError as e:
            print(f"Error: {e}")

    def show_history(self):
        if not self.history:
            print("History is empty.")
        else:
            print("History:")
            for item in self.history:
                for description, value in item.items():
                    print(f'{description.capitalize()}: {value}')
                print("-" * 30)

    def encrypt_text_from_file_and_save(self):
        filename = input("Enter the filename to encrypt and save: ")
        try:
            with open(filename, 'r') as file:
                text = file.read()
            shift = int(input("Please enter shift: "))

            if shift < 0:
                raise ValueError("Shift must be a positive integer"
                                 "")
            encrypted_text = Encryptor.encrypt_word_with_key(text, shift)
            self.history.append({
                "input_text": text,
                "shift": shift,
                "encrypted_text": encrypted_text
            })
            print(f"Given text: {text}")
            print(f"Shift: {shift}")
            print(f"Encrypted text: {encrypted_text}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_to_file(self):
        directory = 'history/'
        filename = input("Enter the filename to save history: ")
        with open(directory + filename, 'w') as file:
            json.dump(self.history, file)
        print(f"History saved to {filename}")

    def import_history_from_file(self):
        filename = input("Enter the filename to import history from: ")
        try:
            with open(filename, 'r') as file:
                imported_history = json.load(file)
            self.history.extend(imported_history)
            print(f"History imported from {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def exit(self):
        choice = input("Do you want to save the history before exiting? (Y/N): ")
        if choice.lower() == 'y':
            self.save_to_file()
        self.__is_running = False
        print("See you next time!")


if __name__ == "__main__":
    app = CipherFacade()
