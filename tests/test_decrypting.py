from decrypting.decrypting import Decryptor
import pytest


@pytest.mark.parametrize("text, shift, expected_result", [
    ("tloia", -3, "world"),
])
def test_should_decrypt_word_with_key_negative_shift(self, text, shift,
                                                     expected_result):
    try:
        Decryptor(shift).decrypt_word_with_key(text)
    except ValueError as e:
        assert str(e) == "Shift must be a non-negative integer."
    else:
        pytest.fail(
            "Expected a ValueError for negative shift but no exception was raised.")


@pytest.mark.parametrize("text, shift, expected_result", [
    ("khoor", 3, "hello"),
])
def test_should_decrypt_word_with_key_positive_shift(self, text, shift,
                                                     expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("cde!123", 2, "abc!123"),
])
def test_should_decrypt_word_with_key_special_characters(self, text, shift,
                                                     expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("Yt gj tw tsw ts gj, ymfy nx ymj vjxyjtrj.", 5, "To be or not to be, that is the "
                                                     "question."),
])
def test_should_decrypt_word_with_key_spaces_and_punctuation(self, text, shift,
                                                      expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("abc", 3, "xyz"),
])
def test_should_decrypt_word_with_key_maximum_shift(self, text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("cęgfhijł", 36, "aąbcćdeę"),
])
def test_should_decrypt_word_with_key_large_shift(self, text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("ćęłźźó", 3, "ąęćżźń"),
])
def test_should_decrypt_word_with_key_polish_characters(self, text, shift,
                                                     expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    (" ", 3, " "),
])
def test_should_decrypt_word_with_key_empty_string(self, text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result
