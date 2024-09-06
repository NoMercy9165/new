from pages.login_page import LoginPage


def test_login_pass(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login(credentials["username"], credentials["password"])
    login_page.assert_text_present_on_page('aleksandr.petrichenko@kupibilet.ru')
