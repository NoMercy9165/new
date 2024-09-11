from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = LoginPageLocators()

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_click(self.locators.AUTH_MODAL_BUTTON)
        self.wait_for_selector_and_fill(self.locators.EMAIL_INPUT, username)
        self.wait_for_selector_and_fill(self.locators.PASSWORD_INPUT, password)
        self.wait_for_selector_and_click(self.locators.SIGN_IN_BUTTON)
