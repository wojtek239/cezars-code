from decrypting.decrytping import Decryptor
import unittest
import pytest


class TestDecryptor(unittest.TestCase):

    @pytest.mark.parametrize("encrypted_word, shift, expected_result", [
        ("tloia", -3, "world"),
    ])
    def test_should_decrypt_word_with_key_negative_shift(self):
        if shift < 0:
            with pytest.raises(ValueError):
                Decryptor(-shift).decrypt_word_with_key(text)
        else:
            actual_result = Decryptor(shift).decrypt_word_with_key(text)
            assert actual_result == expected_result

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("khoor", 3, "hello"),
    ])
    def test_should_decrypt_word_with_key_positive_shift(self):

        actual_result = Decryptor.decrypt_word_with_key("khoor", 3)
        expected_result = "hello"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("cde!123", 2, "abc!123"),
    ])
    def test_should_decrypt_word_with_key_special_characters(self):

        actual_result = Decryptor.decrypt_word_with_key("cde!123", 5)
        expected_result = "abc!123"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("Yt gj tw tsw ts gj, ymfy nx ymj vjxyjtrj.", 5, "To be or not to be, that is"
                                                         " the question."),
    ])
    def test_should_decrypt_word_with_key_spaces_and_punctuation(self):
        actual_result = Decryptor.decrypt_word_with_key("Yt gj tw tsw ts gj, "
                                                        "ymfy nx ymj vjxyjtrj.", 5)
        expected_result = "To be or not to be, that is the question"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("abc", 3, "xyz"),
    ])
    def test_should_decrypt_word_with_key_maximum_shift(self):
        actual_result = Decryptor.decrypt_word_with_key("abc", 3)
        expected_result = "xyz"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("cęgfhijł", 36, "aąbcćdeę"),
    ])
    def test_should_decrypt_word_with_key_large_shift(self):
        actual_result = Decryptor.decrypt_word_with_key("cęgfhijł", 36)
        expected_result = "aąbcćdeę"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        ("ćęłźźó", 3, "ąęćżźń"),
    ])
    def test_should_decrypt_word_with_key_polish_characters(self):
        actual_result = Decryptor.decrypt_word_with_key("ćęłźźó", 3)
        expected_result = "ąęćżźń"
        self.assertEqual(actual_result, expected_result)

    @pytest.mark.parametrize("text, shift, expected_result", [
        (" ", 3, " "),
    ])
    def test_should_decrypt_word_with_key_empty_string(self):
        actual_result = Decryptor.decrypt_word_with_key(" ", 3)
        expected_result = " "
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
