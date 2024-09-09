import time
from pages.address_book_page import AddressBook
from pages.login_page import LoginPage
from data_generators import generate_passenger_data
from pages.profile_page import ProfilePage


def test_add_passenger(browser, credentials):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login(credentials["username"], credentials["password"])

    profile_page = ProfilePage(page)
    address_book = AddressBook(page)

    passenger_data = generate_passenger_data()
    profile_page.go_to_address_book()
    address_book.add_passenger(passenger_data)

    time.sleep(1)
    assert page.locator(f"text={passenger_data['lastname']} {passenger_data['firstname']}").is_visible()
