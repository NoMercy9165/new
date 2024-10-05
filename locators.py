class LoginPageLocators:
    AUTH_MODAL_BUTTON = '[data-testid="open-auth-modal-button"]'
    EMAIL_INPUT = '[data-testid="email-input"]'
    PASSWORD_INPUT = '[data-testid="password-input"]'
    SIGN_IN_BUTTON = '[data-testid="sign-in-button"]'
    VK_SIGN = '[name="social-vk"]'
    NUMBER_INPUT = '[placeholder="Телефон или почта"]'
    BUTTON_CONTINUE = 'text=Продолжить'
    PASSWORD_VK_INPUT = '[autocomplete="current-password"]'
    GOOGLE_SIGN = '.styled__BaseSocialLink-sc-o4axx5-1.guEPVM'
    GOOGLE_INPUT_EMAIL = '[name="identifier"]'
    GOOGLE_BUTTON_CONTINUE = 'text=Далее'
    GOOGLE_INPUT_PASSWORD = '[autocomplete="current-password"]'
    APPLE_SING = "//svg[@name='apple']"
    APPLE_INPUT_EMAIL = '[id="account_name_text_field"]'


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
