from encrypting.encrypting import Encryptor
import unittest


class TestEncryptor(unittest.TestCase):
    def test_should_encrypt_word_with_key_positive_shift(self):
        encryptor = Encryptor(3)
        actual_result = encryptor.encrypt_word_with_key("hello", 3)
        expected_result = "khoor"
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_negative_shift(self):
        encryptor = Encryptor(-3)
        actual_result = encryptor.encrypt_word_with_key("world", 3)
        expected_result = "tloia"
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_special_characters(self):
        encryptor = Encryptor(2)
        actual_result = encryptor.encrypt_word_with_key("abc!123", 2)
        expected_result = "cde!123"
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_spaces_and_punctuation(self):
        encryptor = Encryptor(5)
        actual_result = encryptor.encrypt_word_with_key("To be or not to be, that is "
                                                       "the question.", 5)
        expected_result = "Yt gj tw tsw ts gj, ymfy nx ymj vjxyjtrj."
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_maximum_shift(self):
        encryptor = Encryptor(3)
        actual_result = encryptor.encrypt_word_with_key("xyz", 3)
        expected_result = "abc"
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_large_shift(self):
        encryptor = Encryptor(36)
        actual_result = encryptor.encrypt_word_with_key("aąbcćdeę", 36)
        expected_result = "cęgfhijł"
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_polish_characters(self):
        encryptor = Encryptor(3)
        actual_result = encryptor.encrypt_word_with_key("ąęćżźń", 3)
        expected_result = "ćęłźźó"
        self.assertEqual(actual_result, expected_result)

    def test_should_encrypt_word_with_key_empty_string(self):
        encryptor = Encryptor(3)
        actual_result = encryptor.encrypt_word_with_key("", 3)
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
