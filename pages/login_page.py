import time

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

    def login_vk(self, number, password):
        self.navigate_to()
        self.wait_for_selector_and_click(self.locators.AUTH_MODAL_BUTTON)

        with self.page.expect_popup() as new_page_info:
            self.wait_for_selector_and_click(self.locators.VK_SIGN)

        new_page = new_page_info.value
        new_page.bring_to_front()
        new_page.wait_for_url("https://id.vk.com/*")

        # Создание нового экземляра класса для новой вкладки
        vk_page = BasePage(new_page)

        vk_page.wait_for_selector_and_fill(self.locators.NUMBER_INPUT, number)
        vk_page.wait_for_selector_and_click(self.locators.BUTTON_CONTINUE)
        vk_page.wait_for_selector_and_fill(self.locators.PASSWORD_VK_INPUT, password)
        vk_page.wait_for_selector_and_click(self.locators.BUTTON_CONTINUE)

    def login_google(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_click(self.locators.AUTH_MODAL_BUTTON)

        with self.page.expect_popup() as new_page_info:
            self.wait_for_selector_and_click(self.locators.GOOGLE_SIGN)

        new_page = new_page_info.value
        google_page = BasePage(new_page)

        google_page.wait_for_selector_and_fill(self.locators.GOOGLE_INPUT_EMAIL, username)
        google_page.wait_for_selector_and_click(self.locators.GOOGLE_BUTTON_CONTINUE)
        google_page.wait_for_selector_and_fill(self.locators.GOOGLE_INPUT_PASSWORD, password)
        google_page.wait_for_selector_and_click(self.locators.GOOGLE_BUTTON_CONTINUE)

    def login_apple(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_click(self.locators.AUTH_MODAL_BUTTON)

        with self.page.expect_popup as new_page_info:
            self.wait_for_selector_and_click(self.locators.APPLE_SING)

        new_page = new_page_info
        apple_page = BasePage(new_page)

        apple_page.wait_for_selector_and_fill(self.locators.APPLE_INPUT_EMAIL, username)
        apple_page.press_enter()
        apple_page.wait_for_selector_and_click()