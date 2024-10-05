import pytest
from generators.data_generators import generate_random_credentials


@pytest.fixture
def credentials():
    return {
        "username": "zeus.1991@list.ru",
        "password": "Demon9165max"
    }


@pytest.fixture
def invalid_credentials():
    return generate_random_credentials()


@pytest.fixture
def vk_credentials():
    return {
        "number": "+79692154046",
        "password": ""
    }


@pytest.fixture
def google_credentials():
    return {
        "username": "qa@kupibilet.ru",
        "password": ""
    }


@pytest.fixture()
def apple_credentials():
    return {
        "username": "qa@kupibilet.ru",
        "password": ""
    }