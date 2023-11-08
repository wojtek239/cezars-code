from encrypting.encrypting import Encryptor
import pytest


@pytest.mark.parametrize("text, shift", [
    ("world", -3),
])
def test_should_encrypt_word_with_negative_shift(text, shift):
    with pytest.raises(ValueError) as exc_info:
        Encryptor.encrypt_word_with_key(text, shift)

    assert str(exc_info.value) == "Shift must be a non-negative integer."


@pytest.mark.parametrize("text, shift, expected_result", [
    ("hello", 3, "khoor"),
])
def test_should_encrypt_word_with_positive_shift(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("abc!123", 2, "cde!123"),
])
def test_should_encrypt_word_with_special_characters(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("To be or not to be, that is the question.", 5,
     "Yt gj tw sty yt gj, ymfy nx ymj vzjxynts."),
])
def test_should_encrypt_word_with_spaces_and_punctuation(text, shift,
                                                         expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("xyz", 3, "abc"),
])
def test_should_encrypt_word_with_maximum_shift(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("aąbcćdeę", 36, "cęgfhijł"),
])
def test_should_encrypt_word_with_key_large_shift(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("ąęćżźń", 3, "ćęłźźó"),
])
def test_should_encrypt_word_with_polish_characters(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    (" ", 3, " "),
])
def test_should_encrypt_word_with_empty_string(text, shift, expected_result):
    actual_result = Encryptor.encrypt_word_with_key(text, shift)
    assert actual_result == expected_result

# TODO more examples
