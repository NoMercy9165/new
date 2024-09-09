from pages.base_page import BasePage
from locators import AddressBookPageLocators


class AddressBook(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = AddressBookPageLocators()

    def add_passenger(self, passenger_data):
        self.wait_for_selector_and_click(self.locators.ADD_PASSENGER_BUTTON)

        # Заполнение полей пассажира
        self.wait_for_selector_and_fill(self.locators.PASSPORT_INPUT, passenger_data['passport'])
        self.wait_for_selector_and_fill(self.locators.LASTNAME_INPUT, passenger_data['lastname'])
        self.wait_for_selector_and_fill(self.locators.FIRSTNAME_INPUT, passenger_data['firstname'])
        self.wait_for_selector_and_fill(self.locators.MIDDLENAME_INPUT, passenger_data['middlename'])
        self.wait_for_selector_and_fill(self.locators.DAY_INPUT, passenger_data['birth_date']['day'])

        # Месяц
        month_element = self.page.locator(self.locators.MONTH_SELECT)
        month_element.click()
        self.page.locator(f"//div[contains(text(), '{passenger_data['birth_date']['month']}')]").click()

        # Год
        year_input = self.page.locator(self.locators.YEAR_INPUT)
        year_input.fill(passenger_data['birth_date']['year'])

        # Пол
        gender_locator = (self.locators.GENDER_TOGGLER_ITEM_M if passenger_data['gender'] == 'm'
                          else self.locators.GENDER_TOGGLER_ITEM_F)
        self.wait_for_selector_and_click(gender_locator)

        # Сохранение пасса
        self.wait_for_selector_and_click(self.locators.SAVE_BUTTON)
        self.wait_for_selector_and_click(self.locators.DOWNLOAD_NOTEBOOK_PASSENGERS)

    def delete_passenger(self, passenger_data):
        passenger_locator = self.page.locator(
            f"//div[contains(text(), '{passenger_data['passport']}') and contains(text(), '{passenger_data['lastname']}')]")

        assert passenger_locator.is_visible()
        self.wait_for_selector_and_click(passenger_locator)
        self.wait_for_selector_and_click(self.locators.DELETE_PASSENGER_BUTTON)
        self.wait_for_selector_and_click(self.locators.CONFIRM_DELETE_BUTTON)
