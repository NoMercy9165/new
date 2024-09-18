class LoginPageLocators:
    AUTH_MODAL_BUTTON = '[data-testid="open-auth-modal-button"]'
    EMAIL_INPUT = '[data-testid="email-input"]'
    PASSWORD_INPUT = '[data-testid="password-input"]'
    SIGN_IN_BUTTON = '[data-testid="sign-in-button"]'


class ProfilePageLocators:
    PROFILE_MENU = 'text=zeus.1991@list.ru'
    ADDRESS_BOOK_LINK = 'text=Пассажиры'


class AddressBookPageLocators:
    ADD_PASSENGER_BUTTON = 'text=Добавить пассажира'
    PASSPORT_INPUT = '[data-testid="passport-input"]'
    LASTNAME_INPUT = '[data-testid="lastname-input"]'
    FIRSTNAME_INPUT = '[data-testid="firstname-input"]'
    MIDDLENAME_INPUT = '[data-testid="middlename-input"]'
    DAY_INPUT = '[placeholder="День"]'
    MONTH_SELECT = '[placeholder="Месяц"]'
    YEAR_INPUT = '[placeholder="Год"]'
    GENDER_TOGGLER_ITEM_M = '[data-testid="gender-toggler-item-m"]'
    GENDER_TOGGLER_ITEM_F = '[data-testid="gender-toggler-item-f"]'
    SAVE_BUTTON = 'text=Сохранить'
    DELETE_PASSENGER_BUTTON = 'text=Удалить пассажира'
    CONFIRM_DELETE_BUTTON = 'text=Удалить'
    DOWNLOAD_NOTEBOOK_PASSENGERS = "//span[contains(text(), 'Загрузить ещё')]"


class BonusProgram:
    BONUS_PROGRAM = 'text=Бонусная программа'
    FILL_PROFILE = 'text=Заполните профиль'
    APPLE_APP_LINK = 'svg[name="apple"]'
    GOOGLE_PLAY_LINK = 'svg[name="gplay"]'
    HUAWEI_APP_LINK = 'svg[name="huawei"]'
    SHARE_VK = 'svg[name="social-vk"]'
    SHARE_OK = 'svg[name="social-ok"]'
    SHARE_X = 'svg[name="social-x"]'
