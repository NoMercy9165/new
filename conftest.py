import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from data_generators import generate_random_credentials

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
        "username": "zeus.1991@list.ru",
        "password": "Demon9165max"
    }


@pytest.fixture
def invalid_credentials():
    return generate_random_credentials()


@pytest.fixture(scope="function")
def login(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login(credentials["username"], credentials["password"])
    yield page
