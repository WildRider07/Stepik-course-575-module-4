from selenium.webdriver.common.by import By
#class MainPageLocators():
     

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_MSG = (By.XPATH,"//strong[text() = 'Coders at Work']")
    BASKET_MSG = (By.XPATH,"//p[contains (text(), 'basket')]/strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
       #//div[@id='messages']/div[1]/div
    #div:nth-of-type(1) > .alertinner

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
 
class LoginFormLocators:
    EMAIL = (By.CSS_SELECTOR, "input#id_login-username")
    PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    LOG_IN = (By.CSS_SELECTOR, "button[name='login_submit']")
    FORGOT = (By.CSS_SELECTOR, "#login_form a")

class RegisterFormLocators:
    EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MSG = (By.XPATH, "//p[contains (text(), 'empty')]")