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

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group a")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MSG = (By.XPATH, "//p[contains (text(), 'empty')]")