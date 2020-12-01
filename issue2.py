from morse import decode
import pytest


@pytest.mark.parametrize('msg,expected', [
    ("... --- ...", "SOS"),
    (".-   -...", "AB"),
    (".-          -...", "AB"),
    ("- . ... - -....- - . ... -", "TEST-TEST"),
])
def test_decode(msg: str, expected: str):
    assert decode(msg) == expected
