from encrypting.encrypting import Encryptor
import pytest


@pytest.mark.parametrize("text, shift", [
    ("world", -3),
    ("happy", -10),
    ("blabla", -1)
])
def test_should_encrypt_word_with_negative_shift(text, shift):
    with pytest.raises(ValueError) as exc_info:
        Encryptor.encrypt_word_with_key(text, shift)

    assert str(exc_info.value) == "Shift must be a positive integer"


@pytest.mark.parametrize("text, shift, expected_result", [
    ("hello", 3, "khoor"),
    ("abcd", 1, "bcde"),
    ("cqe", 4, "gui")
])
def test_should_encrypt_word_with_positive_shift(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("abc!123", 2, "cde!123"),
    ("cde!456", 3, "fgh!456"),
    ("sen!998", 4, "wir!998")
])
def test_should_encrypt_word_with_special_characters(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("To be or not to be, that is the question.", 5,
     "Yt gj tw sty yt gj, ymfy nx ymj vzjxynts."),
    ("I really like You, probably the most", 7,
    "P ylhss sprl `v|, wyvihis {ol tvz{"),
    ("How. could. you, do. this..", 10,
     "Rya. myvn. cy, ny. ~rs}..")
])
def test_should_encrypt_word_with_spaces_and_punctuation(text, shift,
                                                         expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("aąbcćdeę", 32, "aąbcćdeę"),
    ("a", 32, "a"),
    ("Halloween", 32, "Halloween")
])
def test_should_encrypt_word_with_maximum_shift(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("xyz", 3, "abc"),
    ("tuw", 6, "")
])
def test_should_encrypt_word_with_key_large_shift(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("ąęćżźń", 3, "ąęćżźń"),
    ("ćććśż", 5, "ćććśż"),
    ("ą", 10, "ą")
])
def test_should_encrypt_word_with_polish_characters(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    (" ", 3, " "),
    ("  ", 5, "  ")
])
def test_should_encrypt_word_with_empty_string(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


