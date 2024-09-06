from pages.account_page import AccountPage


def test_passenger_add(browser, credentials):
    page = browser.new_page()
    account_page = AccountPage(page)

    account_page.settings_notebook(credentials["username"], credentials["password"])
