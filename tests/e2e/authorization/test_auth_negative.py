from pages.login_page import LoginPage


def test_login_fail(browser, invalid_credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login(invalid_credentials["username"], invalid_credentials["password"])
    login_page.assert_text_present_on_page('Вы ошиблись в почте или пароле')
