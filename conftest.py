import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def credentials():
    return {
        "username": "aleksandr.petrichenko@kupibilet.ru",
        "password": "Demon9165max"
    }
