from playwright.sync_api import expect


class BasePage:
    __BASE_URL = 'https://www.kupibilet.ru'

    def __init__(self, page):
        self.page = page
        self.endpoint = ''

    def _get_full_url(self):
        return f"{self.__BASE_URL}/{self.endpoint}"

    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def wait_for_selector_and_type(self, selector, value, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)

    def assert_element_contains_text(self, selector, text, timeout=10000):
        locator = self.page.locator(selector)
        locator.scroll_into_view_if_needed()
        locator.wait_for(timeout=timeout)
        assert text in locator.inner_text()

    def check_link_opens_in_new_tab(self, selector, expected_partial_url):
        with self.page.expect_popup() as new_page_info:
            self.wait_for_selector_and_click(selector)
        new_page = new_page_info.value
        actual_url = new_page.url
        assert expected_partial_url in actual_url


class SupportDropdown:
    def __init__(self, page):
        self.page = page
        self.order_actions = self.page.locator('text=Действия с заказом')
        self.chat = self.page.locator('text=Чат')
        self.faq = self.page.locator('text=Инструкции и FAQ')

    def click_order_actions(self):
        self.order_actions.click()

    def click_chat(self):
        self.chat.click()

    def click_faq(self):
        self.faq.click()


class ProfileDropdown:
    def __init__(self, page):
        self.page = page
        self.orders = self.page.locator('text=Заказы')
        self.bonus_program = self.page.locator('text=Бонусная программа')
        self.subscriptions = self.page.locator('text=Подписки')
        self.passengers = self.page.locator('text=Пассажиры')
        self.settings = self.page.locator('text=Настройки')
        self.logout = self.page.locator('text=Выйти из аккаунта')

    def click_orders(self):
        self.orders.click()

    def click_bonus_program(self):
        self.bonus_program.click()

    def click_subscriptions(self):
        self.subscriptions.click()

    def click_passengers(self):
        self.passengers.click()

    def click_settings(self):
        self.settings.click()

    def click_logout(self):
        self.logout.click()
