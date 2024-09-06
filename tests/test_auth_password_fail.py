from pages.login_page import LoginPage


def test_login_fail(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login('aleksandr.petrichenko@kupibilet.ru', 'Demon9165max!')
    login_page.assert_text_present_on_page('Вы ошиблись в почте или пароле')
