from locators import BonusProgram
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
import pytest


@pytest.mark.usefixtures("login")
class TestNavigation:

    def test_click_fill_profile_link(self, login):
        page = login
        base_page = BasePage(page)
        self.locators = BonusProgram

        profile_page = ProfilePage(page)
        profile_page.go_to_address_book()

        base_page.wait_for_selector_and_click(self.locators.BONUS_PROGRAM)
        base_page.wait_for_selector_and_click(self.locators.FILL_PROFILE)
        base_page.assert_text_present_on_page('Личные данные')

    def test_click_install_app_link(self, login):
        page = login
        base_page = BasePage(page)
        self.locators = BonusProgram

        profile_page = ProfilePage(page)
        profile_page.go_to_address_book()

        base_page.wait_for_selector_and_click(self.locators.BONUS_PROGRAM)
        base_page.check_link_opens_in_new_tab(self.locators.APPLE_APP_LINK, "https://apps.apple.com/ru/app/")

        # base_page.wait_for_selector_and_click(self.locators.BONUS_PROGRAM)
        # base_page.check_link_opens_in_new_tab(self.locators.GOOGLE_PLAY_LINK, "https://play.google.com/store/apps/")

        base_page.wait_for_selector_and_click(self.locators.BONUS_PROGRAM)
        base_page.check_link_opens_in_new_tab(self.locators.HUAWEI_APP_LINK, "https://appgallery.huawei.com/app/")
