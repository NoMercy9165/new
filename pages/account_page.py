from pages.base_page import BasePage
from pages.login_page import LoginPage


class AccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.endpoint = ''

    EMAIL_BUTTON = 'text="aleksandr.petrichenko@kupibilet.ru"'
    SETTINGS_BUTTON = 'text="Настройки"'
    NOTEBOOK = 'text="Записная книжка"'

    def settings_notebook(self, username, password):
        login_page = LoginPage(self.page)
        login_page.login(username, password)
        self.wait_for_selector_and_click(self.EMAIL_BUTTON)
        self.wait_for_selector_and_click(self.SETTINGS_BUTTON)
        self.wait_for_selector_and_click(self.NOTEBOOK)





