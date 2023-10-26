from encrypting.encrypting import Encryptor
import unittest
import pytest


class TestEncryptor(unittest.TestCase):

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("world", -3, "tloia"),
    ])
    def test_should_encrypt_word_with_key(self, shift, text, expected_result):
        if shift < 0:
            with pytest.raises(ValueError):
                Encryptor(-shift).encrypt_word_with_key(text)
        else:
            actual_result = Encryptor(shift).encrypt_word_with_key(text)
            assert actual_result == expected_result

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("hello", 3, "khoor")
    ])
    def test_should_encrypt_word_with_key_positive_shift(self):
        shift = 3
        text_to_encrypt = "hello"
        expected_result = "khoor"
        actual_result = Encryptor.encrypt_word_with_key(text_to_encrypt, shift)

        self.assertEqual(actual_result, expected_result)

#   def test_encrypter_should_raise_exception_for_negative_shift(self):
#        actual_result = Encryptor.encrypt_word_with_key("world", -3)
#        expected_result = "tloia"
#        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("abc!123", 2, "cde!123")
    ])
    def test_should_encrypt_word_with_key_special_characters(self):
        actual_result = Encryptor.encrypt_word_with_key("abc!123", 2)
        expected_result = "cde!123"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("To be or not to be, that is the question.", 5,
         "Yt gj tw tsw ts gj, ymfy nx ymj"
         " vjxyjtrj")
    ])
    def test_should_encrypt_word_with_key_spaces_and_punctuation(self):

        actual_result = Encryptor.encrypt_word_with_key("To be or not to be, that is "
                                                       "the question.", 5)
        expected_result = "Yt gj tw tsw ts gj, ymfy nx ymj vjxyjtrj."
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("xyz", 3, "abc")
    ])
    def test_should_encrypt_word_with_key_maximum_shift(self):
        actual_result = Encryptor.encrypt_word_with_key("xyz", 3)
        expected_result = "abc"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("aąbcćdeę", 36, "cęgfhijł")
    ])
    def test_should_encrypt_word_with_key_large_shift(self):
        actual_result = Encryptor.encrypt_word_with_key("aąbcćdeę", 36)
        expected_result = "cęgfhijł"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("ąęćżźń", 3, "ćęłźźó")
    ])
    def test_should_encrypt_word_with_key_polish_characters(self):
        actual_result = Encryptor.encrypt_word_with_key("ąęćżźń", 3)
        expected_result = "ćęłźźó"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        (" ", 3, " ")
    ])
    def test_should_encrypt_word_with_key_empty_string(self):
        actual_result = Encryptor.encrypt_word_with_key("", 3)
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
