from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    OPEN_AUTH_MODAL = '[data-testid="open-auth-modal-button"]'
    USERNAME_SELECTOR = '[data-testid="email-input"]'
    PASSWORD_SELECTOR = '[data-testid="password-input"]'
    LOGIN_BUTTON_SELECTOR = '[data-testid="sign-in-button"]'

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_click(self.OPEN_AUTH_MODAL)
        self.wait_for_selector_and_type(self.USERNAME_SELECTOR, username, 50)
        self.wait_for_selector_and_type(self.PASSWORD_SELECTOR, password, 50)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
