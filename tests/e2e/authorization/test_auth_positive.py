from pages.login_page import LoginPage


def test_login_pass(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login(credentials["username"], credentials["password"])
    login_page.assert_text_present_on_page('zeus.1991@list.ru')


def test_login_vk_pass(browser, vk_credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login_vk(vk_credentials["number"], vk_credentials["password"])
    login_page.wait_for_url_and_assert('https://www.kupibilet.ru/')
    # login_page.assert_text_present_on_page('tv@kupibilet.ru')


def test_login_google_pass(browser, google_credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login_google(google_credentials["username"], google_credentials["password"])


def test_login_apple_pass(browser, apple_credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login_apple(apple_credentials["username"], apple_credentials["password"])
