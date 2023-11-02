from encrypting.encrypting import Encryptor
import pytest


@pytest.mark.parametrize("text, shift, expected_result", [
    ("world", -3, "tloia"),
])
def test_should_encrypt_word_with_key_negative_shift(self, text, shift,
                                                     expected_result):
    try:
        Encryptor(shift).encrypt_word_with_key(text)
    except ValueError as e:
        assert str(e) == "Shift must be a non-negative integer."
    else:
        pytest.fail(
            "Expected a ValueError for negative shift but no exception was raised.")


@pytest.mark.parametrize("text, shift, expected_result", [
    ("hello", 3, "khoor"),
])
def test_should_encrypt_word_with_key_positive_shift(self, text, shift,
                                                     expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("abc!123", 2, "cde!123"),
])
def test_should_encrypt_word_with_key_special_characters(self, text, shift,
                                                     expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("To be or not to be, that is the question.", 5,
     "Yt gj tw tsw ts gj, ymfy nx ymj vjxyjtrj."),
])
def test_should_encrypt_word_with_key_spaces_and_punctuation(self, text, shift,
                                                      expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("xyz", 3, "abc"),
])
def test_should_encrypt_word_with_key_maximum_shift(self, text, shift, expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("aąbcćdeę", 36, "cęgfhijł"),
])
def test_should_encrypt_word_with_key_large_shift(self, text, shift, expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("ąęćżźń", 3, "ćęłźźó"),
])
def test_should_encrypt_word_with_key_polish_characters(self, text, shift,
                                                     expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    (" ", 3, " "),
])
def test_should_encrypt_word_with_key_empty_string(self, text, shift, expected_result):
    actual_result = Encryptor(shift).encrypt_word_with_key(text)
    assert actual_result == expected_result
