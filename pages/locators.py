from selenium.webdriver.common.by import By
class MainPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_MSG = (By.XPATH,"//strong[text() = 'Coders at Work']")
    BASKET_MSG = (By.XPATH,"//p[contains (text(), 'basket')]/strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
#class LoginPageLocators():
#    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
#    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")