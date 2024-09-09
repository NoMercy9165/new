from pages.base_page import BasePage
from locators import ProfilePageLocators


class ProfilePage(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.locators = ProfilePageLocators()

    def go_to_address_book(self):
        self.wait_for_selector_and_click(self.locators.PROFILE_MENU)
        self.wait_for_selector_and_click(self.locators.ADDRESS_BOOK_LINK)
