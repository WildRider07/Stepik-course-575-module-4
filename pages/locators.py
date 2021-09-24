from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_MSG = (By.CSS_SELECTOR, "div:nth-of-type(1) > .alertinner")
    ADDED_NAME = (By.CSS_SELECTOR, "div:nth-of-type(1) > .alertinner > strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    BASKET_TOTAL_MSG = (By.CSS_SELECTOR, ".alertinner > p:nth-of-type(1)")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner > p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
               
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class RegisterFormLocators:
    EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MSG = (By.XPATH, "//p[contains (text(), 'empty')]")