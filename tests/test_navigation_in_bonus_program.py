from pages.bonus_program_page import BonusProgramPage
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
import pytest
from data.test_data_bonus import INSTALL_APP_LINKS, SOCIAL_APP_LINKS


@pytest.mark.usefixtures("login")
class TestNavigation:

    @pytest.fixture(autouse=True)
    def setup(self, login):
        self.page = login
        self.base_page = BasePage(self.page)
        self.bonus_program_page = BonusProgramPage(self.page)
        self.profile_page = ProfilePage(self.page)
        self.profile_page.go_to_address_book()
        self.base_page.wait_for_selector_and_click(self.bonus_program_page.locators.BONUS_PROGRAM)

    def test_click_fill_profile_link(self):
        self.base_page.wait_for_selector_and_click(self.bonus_program_page.locators.FILL_PROFILE)
        self.base_page.assert_text_present_on_page('Личные данные')

    @pytest.mark.parametrize("link_locator, expected_url", INSTALL_APP_LINKS)
    def test_click_install_app_links(self, link_locator, expected_url):
        self.base_page.check_link_opens_in_new_tab(link_locator, expected_url)

    @pytest.mark.parametrize("social_locator, expected_url", SOCIAL_APP_LINKS)
    def test_click_social_app_links(self, social_locator, expected_url):
        self.base_page.check_link_opens_in_new_tab(social_locator, expected_url)
