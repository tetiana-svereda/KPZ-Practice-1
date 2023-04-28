import pytest
from lab3 import palindrom
from lab3 import validate_ip
from lab3 import get_os


def test_palindrom():
    with pytest.raises(TypeError):
        palindrom()

    with pytest.raises(TypeError):
        palindrom(123)

    assert palindrom("Hello world") == []

    assert palindrom("Anna civic rotor level deed") == ['civic', 'rotor', 'level', 'deed']


def test_validate_ip():
    with pytest.raises(TypeError):
        validate_ip()

    with pytest.raises(TypeError):
        validate_ip(123)

    assert validate_ip('213.109.232.81') == True

    assert validate_ip('256.168.0.1') == False

    assert validate_ip('192.168.0') == False

    assert validate_ip('192.168.256.1') == False


def test_get_os():
    assert get_os() == 'Windows'