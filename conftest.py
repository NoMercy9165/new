import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def login(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login(credentials["username"], credentials["password"])
    yield page
