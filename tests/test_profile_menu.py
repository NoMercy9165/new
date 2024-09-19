from pages.base_page import BasePage
from pages.login_page import LoginPage


def test_click_orders(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(credentials["username"], credentials["password"])

    base_page.profile_button.click()
    base_page.profile_dropdown.click_orders()
    assert base_page.page.url == "https://www.kupibilet.ru/user/orders"
    base_page.assert_text_present_on_page('У вас нет предстоящих поездок')


def test_click_bonus_program(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(credentials["username"], credentials["password"])

    base_page.profile_button.click()
    base_page.profile_dropdown.click_bonus_program()
    assert base_page.page.url == "https://www.kupibilet.ru/user/loyalty"
    base_page.assert_text_present_on_page('Копите баллы и тратьте на поездки')


def test_click_subscriptions(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(credentials["username"], credentials["password"])

    base_page.profile_button.click()
    base_page.profile_dropdown.click_subscriptions()
    assert base_page.page.url == "https://www.kupibilet.ru/user/subscriptions"
    base_page.assert_text_present_on_page('Нет подписок на цены')


def test_click_passengers(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(credentials["username"], credentials["password"])

    base_page.profile_button.click()
    base_page.profile_dropdown.click_passengers()
    assert base_page.page.url == "https://www.kupibilet.ru/user/notebook"
    base_page.assert_text_present_on_page('Записная книжка')


def test_click_settings(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(credentials["username"], credentials["password"])

    base_page.profile_button.click()
    base_page.profile_dropdown.click_settings()
    assert base_page.page.url == "https://www.kupibilet.ru/user/settings"
    base_page.assert_text_present_on_page('Личные данные')


def test_click_logout(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(credentials["username"], credentials["password"])

    base_page.profile_button.click()
    base_page.profile_dropdown.click_logout()
    assert base_page.page.url == "https://www.kupibilet.ru/"
    base_page.assert_text_present_on_page('Сервис билетных лазеек')
