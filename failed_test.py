from morse import encode, decode
import pytest


def test_encode_with_comma():
    with pytest.raises(KeyError):
        encode("SIMPLE TEXT,WITH COMMA")


def test_encode_with_comma_and_space():
    with pytest.raises(KeyError):
        encode("SIMPLE TEXT, WITH COMMA AND SPACE")


def test_encode_and_decode_funcs_are_irreversible():
    test_case = "WITH SPACE"
    assert test_case != decode(encode(test_case))
