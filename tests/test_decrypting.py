from decrypting.decrypting import Decryptor
import pytest


@pytest.mark.parametrize("text, shift", [
    ("tloia", -3),
    ("abdal", -5),
    ("hallah", -10)
])
def test_should_decrypt_word_with_key_negative_shift(text, shift):
    with pytest.raises(ValueError) as exc_info:
        Decryptor.decrypt_word_with_key(text, shift)

        assert str(exc_info.value) == "Shift must be a positive integer"


@pytest.mark.parametrize("text, shift, expected_result", [
    ("khoor", 3, "hello"),
    ("bcde", 1, "abcd"),
    ("gui", 4, "cqe")
])
def test_should_decrypt_word_with_key_positive_shift(text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("cde!123", 2, "abc!123"),
    ("anik!908", 5, "|idf!908"),
    ("asn?77", 3, "~pk?77")
])
def test_should_decrypt_word_with_key_special_characters(text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("Yt gj tw sty yt gj, ymfy nx ymj vzjxynts.", 5, "To be or not to be, that is the "
                                             "question."),
    ("P ylhss sprl `v|, wyvihis {ol tvz{", 7, "I really like You, probably the most"),
    ("Rya. myvn. cy, ny. ~rs}.", 10, "How. could. you, do. this..")
])
def test_should_decrypt_word_with_key_spaces_and_punctuation(text, shift,
                                                             expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("abc", 3, "xyz"),
])
def test_should_decrypt_word_with_key_maximum_shift(text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("cęgfhijł", 32, "cęgfhijł"),
    ("abc", 32, "abc"),
    ("csfjhb 2sx,", 32, "csfjhb 2sx,")
])
def test_should_decrypt_word_with_key_large_shift(text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    ("ćęłźźó", 3, "ćęłźźó"),
    ("ąćź", 10, "ąćź"),
    ("źń", 20, "źń")
])
def test_should_decrypt_word_with_key_polish_characters(text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result


@pytest.mark.parametrize("text, shift, expected_result", [
    (" ", 3, " "),
    (" ", 5, " "),
    (" ", 10, " ")
])
def test_should_decrypt_word_with_key_empty_string(text, shift, expected_result):
    actual_result = Decryptor.decrypt_word_with_key(text, shift)
    assert actual_result == expected_result
