from pages.base_page import BasePage
from locators import BonusProgram


class BonusProgramPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = BonusProgram
